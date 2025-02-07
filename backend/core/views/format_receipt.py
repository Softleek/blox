import logging
import pytz
from django.utils import timezone

def format_receipt(salesinvoice, served_by):
    """Format the sales invoice receipt as a text string for an 80mm POS printer."""
    localized_datetime = salesinvoice.date
     
    def get_day_with_suffix(day):
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
        return f"{day}{suffix}"

    # Extract the day with the correct suffix
    day_with_suffix = get_day_with_suffix(localized_datetime.day)

    # Format date
    formatted_date = localized_datetime.strftime(f'%a, %B {day_with_suffix} %Y at %I:%M %p')
    
    # Receipt Header
    formatted_receipt = (
        "-----------------RECEIPT--------------------------------\n"
        f"Date: {formatted_date}\n"
        "------------------------------------------------------------------------------\n\n"
        "ITEM            QTY   PRICE   TOTAL\n"
        "------------------------------------------------------------------------------\n"
    )
    
    subtotal = 0.0
    for item in salesinvoice.items.all():
        total_price = float(item.quantity) * float(item.rate)
        subtotal += total_price
        
        # Split item name into multiple lines if it exceeds 12 characters
        item_name = item.item.name
        first_line = True  # Track whether it's the first line of a wrapped item name
        while len(item_name) > 12:
            # Find the last space within the first 12 characters to split at
            split_pos = item_name.rfind(' ', 0, 12)
            if split_pos == -1:
                split_pos = 12  # If no space is found, just cut at 12 characters
            line = item_name[:split_pos].rstrip()
            item_name = item_name[split_pos:].lstrip()

            # For the first line, print the whole quantity, price, and total, then wrap the name
            if first_line:
                formatted_receipt += (
                    f"{line:<12} {item.quantity:>4}   {format(item.rate, '.2f'):>6}   {format(total_price, '.2f'):>7}\n"
                )
                first_line = False
            else:
                # For subsequent lines, print only the wrapped item name without repeating qty, price, total
                formatted_receipt += (
                    f"{line:<12}\n"
                )
        
        # After the while loop, if there's any leftover part of the item name, print it
        if item_name:
            if first_line:
                formatted_receipt += (
                    f"{item_name:<12} {item.quantity:>4}   {format(item.rate, '.2f'):>6}   {format(total_price, '.2f'):>7}\n"
                )
            else:
                formatted_receipt += (
                    f"{item_name:<12}\n"
                )

    # Calculate totals
    discount = float(salesinvoice.discount or 0)
    total_after_discount = subtotal - discount

    # Add totals and footer
    formatted_receipt += (
        "------------------------------------------------------------------------------\n\n"
        f"Subtotal:         Ksh {format(subtotal, '.2f'):>12}\n"
        f"Discount:         Ksh {format(discount, '.2f'):>12}\n"
        f"Total:            Ksh {format(total_after_discount, '.2f'):>12}\n"
        "------------------------------------------------------------------------------\n\n"
        "Thank you for your purchase!\n\n"  # Bold text end
        "Contact us: 0724870295\n\n"
        f"Served by: {served_by}\n\n\n"
    )
    
    return formatted_receipt.strip()
