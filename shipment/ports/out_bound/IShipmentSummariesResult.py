from shipment.ports.out_bound.ShipmentSummary import ShipmentSummary


class IMyShipmentsResult:

    def present(self, result: list[ShipmentSummary]):
        pass

    def present_failure(self, reason):
        pass
