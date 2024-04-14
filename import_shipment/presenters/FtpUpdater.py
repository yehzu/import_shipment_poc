from import_shipment.ports.out_bound.ImportMblResult import ImportMblResult
from import_shipment.ports.out_bound.ObImportMblResponse import ObImportMblResponse


class FtpUpdater(ImportMblResult):
    def __init__(self, filename):
        self.filename = filename
        self.view_model = None

    def present_skip(self, msg):
        self.view_model = f'{self.filename}.reject'
        self._upload()

    def present_error(self, msg):
        self.view_model = f'{self.filename}.error'
        self._upload()

    def present(self, resp: ObImportMblResponse):
        self.view_model = f'{self.filename}.ok'
        self._upload()

    def _upload(self):
        # not a good implementation. should move out the upload operation to the controller (django's view)
        # involve side effect here will cause the use case hard to be tested
        # however, it's a POC. just illustrate the concept here.
        ftp.upload(self.view_model)
