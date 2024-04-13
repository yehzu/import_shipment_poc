from background_task import background
from import_shipment.factories.MblGatewayFactory import MblGatewayFactory
from import_shipment.factories.PayloadInterpreterFactory import PayloadInterpreterFactory
from import_shipment.factories.TradePartnerGatewayFactory import TradePartnerGatewayFactory
from import_shipment.presenters.JsonPresenter import JsonPresenter
from import_shipment.presenters.FakePresenter import FakePresenter
from import_shipment.use_cases.UseCases import UseCases
from import_shipment.protocols.FtpReader import FtpReader


# Create your views here.


# handler for route /shipment/fast-pro/xml/v1
def import_fast_pro_xml_v1(request):
    tenant = "test tenant"  # or other way to get tenant, maybe in the header?
    mbl_payload = request.body  # or other way to get the payload (e.g. http body, or AS2 protocol)

    interpreter = PayloadInterpreterFactory.get("fast-pro-xml-v1")
    mbl_repo = MblGatewayFactory.get()
    tp_repo = TradePartnerGatewayFactory.get()

    presenter = JsonPresenter()

    usecase = UseCases()
    usecase.import_mbl(tenant, mbl_payload, interpreter, mbl_repo, tp_repo, presenter)

    return presenter.get_view_model()


def import_fast_pro_xml_ftp(payload):
    tenant = "test tenant"  # or other way to get tenant, maybe in the header?
    mbl_payload = payload

    interpreter = PayloadInterpreterFactory.get("fast-pro-xml-v1")
    mbl_repo = MblGatewayFactory.get()
    tp_repo = TradePartnerGatewayFactory.get()

    presenter = FakePresenter()

    usecase = UseCases()
    usecase.import_mbl(tenant, mbl_payload, interpreter, mbl_repo, tp_repo, presenter)

    return presenter.get_view_model()


@background(schedule=10)
def import_fast_pro_ftp_schedule():
    ftp = FtpReader()
    ftp.get_file_content('path', import_fast_pro_xml_ftp)
