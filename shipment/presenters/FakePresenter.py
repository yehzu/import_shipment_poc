import json
from datetime import datetime

from shipment.ports.out_bound.IShipmentSummariesResult import IShipmentSummariesResult
from shipment.ports.out_bound.ShipmentSummary import ShipmentSummary


class FakePresenter(IShipmentSummariesResult):
    def present(self, result: list[ShipmentSummary]):
        class Encoder(json.JSONEncoder):
            def default(self, o):
                if isinstance(o, datetime):
                    return str(o)
                return o.__dict__

        print(json.dumps(result, cls=Encoder))

    def present_failure(self, reason):
        print(reason)
