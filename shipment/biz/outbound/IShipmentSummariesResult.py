from shipment.biz.outbound.ShipmentSummary import ShipmentSummary


class IShipmentSummariesResult:

    def present(self, result: list[ShipmentSummary]):
        pass

    def present_failure(self, reason):
        pass
