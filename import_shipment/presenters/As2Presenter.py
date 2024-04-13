from import_shipment.ports.Presenter import Presenter
from import_shipment.ports.out_bound.ImportMblResult import ImportMblResult


class As2Presenter(ImportMblResult, Presenter):
    def __init__(self):
        self.view_model = None

    def get_view_model(self):
        return self.view_model

    def present(self, msg):
        self.view_model = msg
