from import_shipment.ports.gateways.PayloadInterpreter import PayloadInterpreter
from import_shipment.entities.Mbl import Mbl


class EdiAdapter(PayloadInterpreter):
    def interpret_payload(self, payload) -> Mbl:
        # parse x12 format into MBL model
        # here is a fake
        mbl = Mbl()
        mbl.mbl_number = payload[0:30]
        return mbl
