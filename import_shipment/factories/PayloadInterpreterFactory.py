from import_shipment.adapters.FakePayloadInterpreter import FakePayloadInterpreter
from import_shipment.adapters.FastProXmlV1Adapter import FastProXmlV1Adapter
from import_shipment.adapters.EdiAdapter import EdiAdapter


class PayloadInterpreterFactory():
    @staticmethod
    def get(adapter_type="fake-local-dev"):
        if adapter_type == "fast-pro-xml-v1":
            return FastProXmlV1Adapter()
        if adapter_type == "edi":
            return EdiAdapter()
        if adapter_type == "fake-local-dev":
            return FakePayloadInterpreter()
        else:
            raise NotImplementedError

# A fake, can be used for local development
