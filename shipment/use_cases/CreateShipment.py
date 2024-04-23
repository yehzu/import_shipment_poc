from shipment.ports.gateways.ContainerGateway import ContainerGateway
from shipment.ports.gateways.InvoiceGateway import InvoiceGateway
from shipment.ports.gateways.ShipmentDetailPayloadInterpreter import ShipmentDetailPayloadInterpreter
from shipment.ports.gateways.ShipmentGateway import ShipmentGateway
from shipment.ports.in_bound.ICreateShipment import ICreateShipment
from shipment.ports.out_bound.ICreateShipmentResult import ICreateShipmentResult


class CreateShipment(ICreateShipment):

    def __init__(self,
                 payload_interpreter: ShipmentDetailPayloadInterpreter,
                 shipment_gw: ShipmentGateway,
                 container_gw: ContainerGateway,
                 invoice_gw: InvoiceGateway,
                 presenter: ICreateShipmentResult):
        self.payload_interpreter = payload_interpreter
        self.shipment_gw = shipment_gw
        self.container_gw = container_gw
        self.invoice_gw = invoice_gw
        self.presenter = presenter

    def create_shipment_from_payload(self, tenant, office, my_role, payload):
        sd = self.payload_interpreter.interpret(payload)

        try:
            c_ids = self.container_gw.get_or_create_containers(tenant, office, sd.containers)
            i_ids = self.invoice_gw.get_or_create_invoices(tenant, office, sd.invoices)

            # update the ids to the shipment
            sd.container_ids = c_ids
            sd.invoice_ids = i_ids

            # create
            s_id = self.shipment_gw.create_shipment(tenant, office, my_role, sd)
        except:
            self.presenter.present_failure("fail to create shipment")
            # handle roll back process here
            return

        self.presenter.present(s_id)
