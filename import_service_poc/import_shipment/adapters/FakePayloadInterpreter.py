from import_shipment.entities.Mbl import Mbl
from import_shipment.ports.in_bound.PayloadInterpreter import PayloadInterpreter


class FakePayloadInterpreter(PayloadInterpreter):

    def interpret_payload(self, payload) -> Mbl:
        mbl = Mbl()
        mbl.mbl_number = "1"
        mbl.vessel = "fake vessel"
        mbl.trade_partner = "fake trade_partner"
        return mbl
