from shipment.entities.Shipment import Shipment, InvoiceBalance, Container
from shipment.ports.gateways.ContainerGateway import ContainerGateway
from shipment.ports.gateways.InvoiceGateway import InvoiceGateway
from shipment.ports.gateways.ShipmentGateway import ShipmentGateway


def _create_shipments():
    s1 = Shipment(
        id="1",
        mbl_number=f"MBL_NUM_1",
        invoice_ids=["1", "3", "8"],
        container_ids=["2", "5", "3"])
    s2 = Shipment(
        id="2",
        mbl_number=f"MBL_NUM_2",
        invoice_ids=["2", "4", "5"],
        container_ids=["1", "4", "6"])
    s3 = Shipment(
        id="3",
        mbl_number=f"MBL_NUM_3",
        invoice_ids=["9", "10", "11"],
        container_ids=["7", "8", "9"])

    shipments = [s1, s2, s3]

    balances = {
        s1: (InvoiceBalance(amount=100, invoice_type="AR"), InvoiceBalance(amount=200, invoice_type="AP")),
        s2: (InvoiceBalance(amount=40, invoice_type="AR"), InvoiceBalance(amount=-120, invoice_type="AP")),
        s3: (InvoiceBalance(amount=50, invoice_type="AR"), InvoiceBalance(amount=1000, invoice_type="AP")),
    }

    containers = {
        s1: [Container(id="2", container_number="no 2", size="40GP"),
             Container(id="5", container_number="no 5", size="40GP"),
             Container(id="3", container_number="no 3", size="20GP")],
        s2: [Container(id="1", container_number="no 1", size="20GP"),
             Container(id="4", container_number="no 4", size="20GP"),
             Container(id="6", container_number="no 6", size="20GP")],
        s3: [Container(id="7", container_number="no 7", size="40GP"),
             Container(id="8", container_number="no 8", size="40GP"),
             Container(id="9", container_number="no 9", size="40GP")],
    }

    return shipments, balances, containers


class FakeAdapter(ContainerGateway, InvoiceGateway, ShipmentGateway):

    def __init__(self):
        self.shipments, self.balances, self.containers = _create_shipments()

    def get_containers_per_shipment(self, tenant, shipments) -> dict[Shipment, list[Container]]:
        return self.containers

    def get_balances_per_shipment(self, tenant, shipments) -> dict[Shipment, tuple[InvoiceBalance, InvoiceBalance]]:
        return self.balances

    def get_shipments(self, tenant, office, my_role) -> list[Shipment]:
        return self.shipments
