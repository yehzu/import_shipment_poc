from import_shipment.ports.in_bound.IImportShipment import IImportShipment


class ImportShipmentController:
    def handle(self, use_case: IImportShipment, tenant: str, payload: str):
        # controller, which invokes use_case
        use_case.import_mbl(tenant, payload)
