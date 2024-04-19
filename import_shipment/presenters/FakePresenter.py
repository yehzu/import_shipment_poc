from import_shipment.ports.Presenter import Presenter
from import_shipment.ports.out_bound.ObImportMblResponse import ObImportMblResponse
from import_shipment.ports.out_bound.ImportMblResult import ImportMblResult


class FakePresenter(ImportMblResult, Presenter):
    def present(self, ob_mbl: ObImportMblResponse):
        print(f"mbl number: {ob_mbl.mbl_number}, status: {ob_mbl.status}")

    def get_view_model(self):
        super().get_view_model()
