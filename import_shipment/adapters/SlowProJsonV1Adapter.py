import json

from import_shipment.entities.Mbl import Mbl
from import_shipment.ports.gateways.PayloadInterpreter import PayloadInterpreter


class SlowProJsonV1Adapter(PayloadInterpreter):

    def interpret_payload(self, payload) -> Mbl:
        # suppose the payload is
        # {"shipment number": "123", "client": "Apple"}

        obj = json.loads(payload)
        mbl = Mbl()
        mbl.mbl_number = obj['shipment number']
        mbl.trade_partner = obj['client']

        return mbl
