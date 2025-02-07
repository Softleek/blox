import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from pos_app.models.sales import SalesInvoice, SalesInvoiceItem, Payment, Commission, PaymentMethod
from pos_app.models.inventory import Item, StockLedger
from django.utils import timezone
from .receipt_printer import ReceiptPrinter  # Import the ReceiptPrinter class
from .format_receipt import format_receipt  # Import the format_receipt function
from django.db.models import F, Q, Sum
from datetime import datetime, timedelta
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

# Set up logger
logger = logging.getLogger(__name__)


class InvoicePrintAPIView(APIView):

    def post(self, request):
        try:
            # Extract data from request
            data = request.data
            id = data.get('id')
            salesinvoice = SalesInvoice.objects.get(pk=id)
            
            formatted_receipt = format_receipt(salesinvoice, request.user.first_name)

            # Initialize and connect to the printer
            receipt_printer = ReceiptPrinter()  # Replace with your printer's IP address
            receipt_printer.connect()

            # Print the formatted receipt
            receipt_printer.print_receipt(formatted_receipt)
            return Response({'success': 'Successfully printed receipt'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error processing sales invoice: {str(e)}", exc_info=True)
            return Response(
                {"error": "An error occurred while processing the sales invoice."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


        
class SalesInvoiceAPIView(APIView):

    def post(self, request):
        try:
            # Wrap everything in an atomic transaction
            with transaction.atomic():
                # Extract data from request
                data = request.data
                amount = float(data.get('total', 0))
                items_data = data.get('items', [])
                transaction_code = data.get('transactionCode')
                transaction_method = data.get('transactionMethod')
                commission = float(data.get('commission', 0))
                discount = float(data.get('discount', 0))

                # Create SalesInvoice object
                salesinvoice = SalesInvoice.objects.create(
                    date=timezone.now(),
                    amount=amount,
                    discount=discount,
                    commission=commission,
                    status='Unpaid'  # Default status
                )

                # Process and save items
                for item_data in items_data:
                    item_id = item_data.get('id')
                    quantity = float(item_data.get('quantity', 1))
                    unit_price = float(item_data.get('price', 0))  # Use selling_rate for unit_price

                    # Fetch the Item object
                    item = Item.objects.select_for_update().get(id=item_id)
                    total_price = quantity * unit_price

                    # Create SalesInvoiceItem
                    invoice_item = SalesInvoiceItem.objects.create(
                        item=item,
                        amount=total_price,
                        quantity=quantity,
                        rate=unit_price
                    )

                    # Update item stock
                    old_source_quantity = float(item.stock_quantity)
                    new_source_quantity = old_source_quantity - quantity
                    if new_source_quantity < 0:
                        raise ValueError(f"Insufficient stock for item ID {item_id}")

                    item.stock_quantity = new_source_quantity
                    item.save()

                    # Create StockLedger entry
                    StockLedger.objects.create(
                        item=item,
                        old_quantity=old_source_quantity,
                        new_quantity=new_source_quantity,
                        change=-quantity,
                        transaction_type="Outbound",
                        reference="sale",
                        reference_id=salesinvoice.id,
                        datetime=timezone.now()
                    )

                    # Add the item to the sales invoice
                    salesinvoice.items.add(invoice_item)

                # If commission exists, create Commission record
                if commission > 0:
                    commission_obj = Commission.objects.create(
                        date=timezone.now(),
                        amount=commission,
                    )

                # Create Payment object
                payment = Payment.objects.create(
                    payment_date=timezone.now(),
                    amount=amount,
                    transactioncode=transaction_code,
                    sales_invoice=salesinvoice,
                    payment_method=PaymentMethod.objects.get(pk=transaction_method),
                )

                # Update salesinvoice status based on payment
                salesinvoice.status = 'Paid' if amount > 0 else 'Unpaid'
                salesinvoice.save()

                # Format the receipt for printing
                formatted_receipt = format_receipt(salesinvoice, request.user.first_name)

                # Initialize and connect to the printer
                receipt_printer = ReceiptPrinter("192.168.1.115")  # Replace with your printer's IP
                receipt_printer.connect()

                # Print the formatted receipt
                receipt_printer.print_receipt(formatted_receipt)

                return Response({
                    "id": salesinvoice.id,
                    "amount": salesinvoice.amount,
                    "status": salesinvoice.status,
                    "payment_id": payment.id,
                    "items": [
                        {
                            "id": item.item.id,
                            "quantity": item.quantity,
                            "total_price": item.amount,
                        }
                        for item in salesinvoice.items.all()
                    ],
                    "datetime": salesinvoice.date,
                }, status=status.HTTP_201_CREATED)

        except Item.DoesNotExist:
            return Response({"error": "Item not found."}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as ve:
            return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error processing sales invoice: {str(e)}", exc_info=True)
            return Response(
                {"error": "An error occurred while processing the sales invoice."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

            

class SalesReportView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # 1. Total Revenue
            total_revenue = SalesInvoice.objects.aggregate(totalRevenue=Sum('amount'))['totalRevenue'] or 0
            
            # 2. Units Sold
            units_sold = SalesInvoiceItem.objects.aggregate(total_units_sold=Sum('quantity'))['total_units_sold'] or 0

            # 3. Growth Percentage: Calculate revenue growth compared to a previous period (e.g., last month)
            current_date = datetime.now()
            last_month = current_date - timedelta(days=30)
            previous_period_revenue = SalesInvoice.objects.filter(datetime__lt=last_month).aggregate(previousRevenue=Sum('amount'))['previousRevenue'] or 0
            
            growth_percentage = (
                ((total_revenue - previous_period_revenue) / previous_period_revenue) * 100
                if previous_period_revenue > 0 else 0
            )

            # 4. Volume Change: Percentage change in the number of units sold compared to the previous period
            previous_period_units_sold = SalesInvoiceItem.objects.filter(
                ItemsSalesinvoice__datetime__lt=last_month  # Use the correct related_name here
            ).aggregate(previous_units_sold=Sum('quantity'))['previous_units_sold'] or 0
            
            volume_change = (
                ((units_sold - previous_period_units_sold) / previous_period_units_sold) * 100
                if previous_period_units_sold > 0 else 0
            )

            # 5. Top Products by quantity sold
            top_products = SalesInvoiceItem.objects.values('item__name').annotate(
                total_quantity=Sum('quantity')
            ).order_by('-total_quantity')[:5]

            return Response({
                "totalRevenue": total_revenue,
                "growthPercentage": growth_percentage,
                "unitsSold": units_sold,
                "volumeChange": volume_change,
                "topProducts": list(top_products),
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StockReportView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Current stock levels per item
            current_stock_levels = Item.objects.annotate(
                current_stock=F('stock_quantity')
            ).values('name', 'current_stock', 'minimum_stock_level')

            # Products that need reordering (where stock is less than minimum level)
            products_to_reorder = Item.objects.filter(
                Q(stock_quantity__lt=F('minimum_stock_level')) | Q(minimum_stock_level__isnull=True, stock_quantity__lte=5)
            ).values('id', 'name', 'stock_quantity', 'minimum_stock_level')


            return Response({
                "currentStockLevels": list(current_stock_levels),
                "productsToReorder": list(products_to_reorder),
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
