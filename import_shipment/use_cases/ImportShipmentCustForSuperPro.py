from import_shipment.ports.in_bound.IImportShipment import IImportShipment

from import_shipment.ports.gateways.PayloadInterpreter import PayloadInterpreter
from import_shipment.ports.out_bound.ImportMblResult import ImportMblResult


class ImportShipmentCustForSuperPro(IImportShipment):

    def __init__(self, payload_interpreter: PayloadInterpreter, other_gw, presenter: ImportMblResult):
        # you can inject any dependencies needed for this new flow from here
        self.payload_interpreter = payload_interpreter
        self.other_gw = other_gw
        self.presenter = presenter

    def import_mbl(self, tenant: str, payload: str):
        # ok.... you have a different flow for importing...
        # We can have a new implement for you, without modifying the
        # existing one (import_shipment/use_cases/ImportShipment.py)
        # we can handle this situation through open-closed principle
        mbl = self.payload_interpreter.interpret_payload(payload)
        other_gw.do_something(mbl)
        self.presenter.present("success!")
