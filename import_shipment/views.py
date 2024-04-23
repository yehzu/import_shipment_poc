from import_shipment.factories.MblGatewayFactory import MblGatewayFactory
from import_shipment.factories.PayloadInterpreterFactory import PayloadInterpreterFactory
from import_shipment.factories.TradePartnerGatewayFactory import TradePartnerGatewayFactory
from import_shipment.presenters.JsonPresenter import JsonPresenter
from import_shipment.use_cases.ImportShipment import ImportShipment
from import_shipment.protocols.AS2Decoder import As2Decoder
from import_shipment.presenters.As2Presenter import As2Presenter


# Create your views here.


# handler for route /shipment/fast-pro/xml/v1
def import_fast_pro_xml_v1(request):
    tenant = "test tenant"  # or other way to get tenant, maybe in the header?
    mbl_payload = request.body  # or other way to get the payload (e.g. http body, or AS2 protocol)

    interpreter = PayloadInterpreterFactory.get("fast-pro-xml-v1")
    mbl_repo = MblGatewayFactory.get()
    tp_repo = TradePartnerGatewayFactory.get()

    presenter = JsonPresenter()
    usecase = ImportShipment(interpreter, mbl_repo, tp_repo, presenter)

    usecase.import_mbl(tenant, mbl_payload)

    return presenter.get_view_model()


def import_by_edi_over_as2(request):
    key = "load from somewhere"
    cert = "load from somewhere"

    as2_decoder = As2Decoder(key, cert)
    mbl_payload = as2_decoder.decode(request.META, request.body)

    tenant = "test tenant"  # or other way to get tenant, maybe in the header?

    interpreter = PayloadInterpreterFactory.get("edi")
    mbl_repo = MblGatewayFactory.get()
    tp_repo = TradePartnerGatewayFactory.get()

    presenter = As2Presenter()

    usecase = ImportShipment(interpreter, mbl_repo, tp_repo, presenter)
    usecase.import_mbl(tenant, mbl_payload)

    return presenter.get_view_model()
