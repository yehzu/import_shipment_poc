from import_shipment.use_cases.CustomizedUseCasesA import CustomizedUseCasesA
from import_shipment.use_cases.CustomizedUseCasesB import CustomizedUseCasesB
from import_shipment.use_cases.UseCases import UseCases


class ImportShipmentUseCaseFactory:

    @staticmethod
    def get(tenant, office):
        match (tenant, office):
            case ("t1", "o2"):
                return CustomizedUseCasesA()
            case ("t2", "o3"):
                return CustomizedUseCasesB()
            case _:
                return UseCases()

