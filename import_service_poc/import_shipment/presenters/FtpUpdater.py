from import_service_poc.import_shipment.ports.out_bound.ImportMblResult import ImportMblResult
from import_service_poc.import_shipment.ports.out_bound.ObImportMblResponse import ObImportMblResponse


class FtpUpdater(ImportMblResult):

    def __init__(self, filename):
        self.filename = filename

    def present(self, resp: ObImportMblResponse):
        # write the status file according to the original filename
        if resp.status == "created":
            status_file = f'{self.filename}.ok'
        elif resp.status == "existed":
            status_file = f'{self.filename}.reject'
        else:
            status_file = f'{self.filename}.error'

        # client lib for ftp upload, for example
        # ftp.upload(status_file)

