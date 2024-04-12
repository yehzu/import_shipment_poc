# This is a sample Python script.
from datetime import datetime


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# this is business domain object. must not depend on any other library or non-business domain objects
class MBL:
    mbl_number: str
    vessel: str
    eta: datetime
    trade_partner: str
    # and other business domain fields



class FastProXmlV1Adapter:
    def convert(self, request) -> MBL:
        # convert fast pro protocol to MBL class here
        # for example
        xml = xml_parser.parse(request)
        mbl = MBL()
        mbl.mbl_number = xml[0]['number']
        mbl.vessel = xml[0]['ves_name']
        mbl.trade_partner = xml[0]['client']

        return mbl






class TradePartnerMapper:
    def __init__(self, tp_repo, tenant)
        self.tp_repo = tp_repo
        self.tenant = tenant

    def map(self, trade_partner: str):
        return self.tp_repo.find_most_similar(self.tenant, trade_partner)


class OutBoundMBL:
    mbl_number: str
    vessel: str
    eta: datetime
    trade_partner: str


class UseCases:
    @staticmethod
    def import_mbl(tenant, mbl_payload, adapter, mbl_repo, tp_repo, presenter):
        mbl = adapter.convert(mbl_payload)

        # business logic put here
        if mbl_repo.exist(mbl.mbl_number):
            # do nothing if mbl existed
            return None

        tp_mapper = TradePartnerMapper(tp_repo, tenant)
        ob_mbl = OutBoundMBL()
        ob_mbl.mbl_number = mbl.mbl_number
        ob_mbl.vessel = mbl.vessel
        ob_mbl.trade_partner = tp_mapper.map(mbl.trade_partner)

        # produce side effect to the world
        presenter.present(ob_mbl)



class AdapterFactory:
    @staticmethod
    def get_adapter(adapter_type):
        if adapter_type == "fast-pro-xml-vq":
            return FastProXmlV1Adapter()
        else:
            raise NotImplementedError

class MblRepositoryFactory:
    @staticmethod
    def get_repo(repo_type="gofreight-external-api"):
        if repo_type == "gofreight-external-api":
            return GoFreightGateway()
        elif repo_type == "fake-local-dev":
            return FakeMblRepo()
        else:
            raise NotImplementedError

class TradePartnerRepositoryFactory:
    @staticmethod
    def get_repo(repo_type=""):
        if repo_type == "gofreight-external-api":
            return GoFreightGateway()
        elif repo_type == "fake-local-dev":
            return FakeTPRepo()
        else:
            raise NotImplementedError

class GoFreightGateway:
    gofreight_client = gofreight_lib # client lib for accessing external api
    def exist(self, mbl_number: str) -> bool:
        return self.gofreight_client.get_mbl(mbl_number) is not None

    def find_most_similar(self, tenant, trade_partner):
        tp_list = self.gofreight_client.get_trade_partners(tenant)
        # logic for lookup most similar tp by trade_partner from tp_list
        # here just assign self to the most similar
        most_similar_tp = trade_partner
        return most_similar_tp

    def present(self, ob_mbl: OutBoundMBL):
        # translate ob_mbl to client parameter
        gofreight_client.post_mbl(ob_mbl)



# A fake, can be used for local development
class FakeMblRepo:
    def exist(self, mbl_number: str) -> bool:
        return True

class FakeTpRepo:
    def find_most_similar(self, tenant, trade_partner):
        return "hahahaha: " + trade_partner # just a fake

# handler for route /shipment/fast-pro/xml/v1
def import_fast_pro_xml_v1(request):
    tenant = request['header']['tenant'] # or other way to get tenant, maybe in the header?
    mbl_payload = request['body']
    adapter = AdapterFactory.get_adapter("fast-pro-xml-v1")

    mbl_repo = MblRepositoryFactory.get_repo("gofreight-external-api")
    tp_repo = TradePartnerRepositoryFactory.get_repo("gofreight-external-api")

    presenter = GoFreightGateway()

    UseCases.import_mbl(tenant, mbl_payload, adapter, mbl_repo, tp_repo, presenter)










