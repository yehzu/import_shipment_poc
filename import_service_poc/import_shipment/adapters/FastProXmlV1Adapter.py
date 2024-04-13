from import_shipment.entities.Mbl import Mbl
from import_shipment.ports.in_bound.PayloadInterpreter import PayloadInterpreter
from xml.dom.minidom import parse


class FastProXmlV1Adapter(PayloadInterpreter):
    def interpret_payload(self, payload) -> Mbl:
        super().interpret_payload(payload)
        # convert fast pro protocol to MBL class here
        # for example
        xml = parse(payload)
        mbl = Mbl()
        mbl.mbl_number = xml.getElementsByTagName('number')
        mbl.vessel = xml.getElementsByTagName('ves_name')
        mbl.trade_partner = xml.getElementsByTagName('tp')

        return mbl
