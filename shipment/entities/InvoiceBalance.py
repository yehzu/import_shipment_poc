import decimal
from datetime import datetime


class InvoiceBalance:
    amount: decimal
    currency: str
    last_paid_date: datetime
    invoice_type: str
