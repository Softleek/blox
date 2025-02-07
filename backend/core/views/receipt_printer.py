import logging
import pytz
from django.utils import timezone
import win32print
import win32ui
from win32con import *

logger = logging.getLogger(__name__)

class ReceiptPrinter:
    def __init__(self, printer_name=None):
        """Initialize the ReceiptPrinter with an optional printer name."""
        self.printer_name = printer_name or win32print.GetDefaultPrinter()
        self.hdc = None

    def connect(self):
        """Connect to the printer."""
        if not self.printer_name:
            logger.error("No printer specified or found.")
            return False

        try:
            logger.info(f"Connecting to printer: {self.printer_name}")
            self.hdc = win32ui.CreateDC()
            self.hdc.CreatePrinterDC(self.printer_name)
            return True
        except Exception as e:
            logger.error(f"Error connecting to printer: {str(e)}", exc_info=True)
            return False

   
    def print_receipt(self, formatted_receipt):
        """Print the formatted receipt using the connected printer."""
        if not self.hdc:
            logger.error("Printer is not connected. Call connect() first.")
            return


        try:
            self.hdc.StartDoc("Receipt")
            self.hdc.StartPage()

            # Set font for readability
            font = win32ui.CreateFont({
                "name": "Courier New",  # Monospace for better alignment
                "height": 23,  # Adjust height for readability
                "weight": 600,  # Regular weight
            })
            self.hdc.SelectObject(font)

            # Print line by line
            lines = formatted_receipt.split("\n")
            x_position = 0
            y_position = 0
            line_height = 26

            for line in lines:
                self.hdc.TextOut(x_position, y_position, line)
                y_position += line_height

                # If the content exceeds the printable area, start a new page
                if y_position > 800:
                    self.hdc.EndPage()
                    self.hdc.StartPage()
                    y_position = 0

            self.hdc.EndPage()
            self.hdc.EndDoc()
            logger.info("Receipt printed successfully.")

        except Exception as e:
            logger.error(f"Error printing receipt: {str(e)}", exc_info=True)

        finally:
            self.hdc.DeleteDC()
