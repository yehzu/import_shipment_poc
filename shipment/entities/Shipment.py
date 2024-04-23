import decimal
from datetime import datetime


class Shipment:
    id: str
    mbl_number: str
    container_ids: list[str]
    invoice_ids: list[str]

    def __init__(self, id, mbl_number, container_ids, invoice_ids):
        self.id = id
        self.mbl_number = mbl_number
        self.container_ids = container_ids
        self.invoice_ids = invoice_ids


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


class Container:
    id: str
    container_number: str
    size: str

    def __init__(self, id, container_number, size):
        self.id = id
        self.container_number = container_number
        self.size = size


class Invoice:
    id: str
    invoice_number: str
    invoice_type: str
    amount: decimal


class ShipmentDetail(Shipment):
    containers: list[Container]
    invoices: list[Invoice]
