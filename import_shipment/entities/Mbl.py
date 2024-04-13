# this is business domain object. must not depend on any other library or non-business domain objects
from datetime import datetime


class Mbl:
    mbl_number: str = ""
    vessel: str = ""
    eta: datetime = ""
    trade_partner: str = ""
    # and other business domain fields

