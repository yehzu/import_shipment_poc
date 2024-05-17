from import_shipment.biz.entities.Mbl import Mbl
from import_shipment.biz.gateways.PayloadInterpreter import PayloadInterpreter
from xml.dom.minidom import parseString


class FastProXmlV1Adapter(PayloadInterpreter):
    def interpret_payload(self, payload) -> Mbl:
        super().interpret_payload(payload)
        # convert fast pro protocol to MBL class here
        # for example
        xml = parseString(payload)
        mbl = Mbl()
        mbl.mbl_number = xml.getElementsByTagName('name')[0].firstChild.nodeValue

        return mbl
