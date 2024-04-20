import decimal
from datetime import datetime


class ShipmentSummary:
    mbl_number: str
    container_numbers: list[str]
    container_sizes: list[str]
    ap_balance_amount: decimal
    ap_balance_currency: str
    ap_last_paid_date: datetime
    ar_balance_amount: decimal
    ar_balance_currency: str
    ar_last_paid_date: datetime
