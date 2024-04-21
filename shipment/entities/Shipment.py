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
