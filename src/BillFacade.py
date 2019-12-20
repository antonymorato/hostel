from src import bill
from src.electricalAppliance import ElectricalAppliance
class BillFacade:
    def __init__(self):
        self.__bill = bill()
        self.__electricalAppliance = ElectricalAppliance()

    def getStudentName(self):
        pass


