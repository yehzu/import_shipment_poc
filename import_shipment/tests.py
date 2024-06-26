from django.test import TestCase

from import_shipment.adapters.FakeMblAdapter import FakeMblAdapter
from import_shipment.adapters.FakeTradePartnerAdapter import FakeTradePartnerAdapter
from import_shipment.factories.PayloadInterpreterFactory import PayloadInterpreterFactory
from import_shipment.presenters.JsonPresenter import JsonPresenter
from import_shipment.use_cases.ImportShipment import ImportShipment


# Create your tests here.
class ImportShipmentTest(TestCase):
    def test_import_shipment(self):
        adapter = PayloadInterpreterFactory.get()

        mbl_repo = FakeMblAdapter()
        tp_repo = FakeTradePartnerAdapter()

        presenter = JsonPresenter()

        usecase = ImportShipment(adapter, mbl_repo, tp_repo, presenter)
        usecase.import_mbl("1", "fake payload")
