import decimal
from datetime import datetime


class ContainerSummary:
    container_number: str
    container_size: str


class BalanceSummary:
    balance_amount: decimal
    balance_currency: str
    last_paid_date: datetime


class ShipmentSummary:
    mbl_number: str
    containers: list[ContainerSummary]
    ar: BalanceSummary
    ap: BalanceSummary
