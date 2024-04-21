import decimal
from datetime import datetime


class InvoiceBalance:
    amount: decimal
    currency: str
    last_paid_date: datetime
    invoice_type: str

    def __init__(self, amount, invoice_type, currency="USD", last_paid_date=datetime.today()):
        self.amount = amount
        self.currency = currency
        self.invoice_type = invoice_type
        self.last_paid_date = last_paid_date
