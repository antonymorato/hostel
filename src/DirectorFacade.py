from src.BillFacade import BillFacade
from src.studentFacade import StudentFacade


class DirectorFacade:
    def __init__(self, dict):
        # self.__billFacade = BillFacade()
        self.__studentFacade = StudentFacade(dict)
        return None

    def getStudent(self, field):
        return self.__studentFacade.getStudent()

    def getRoom(self):
        return self.__studentFacade.getRoom()

    def setRoom(self):
        self.__studentFacade.setRoom()

    def removeStudent(self):
        self.__studentFacade.removeStudent()

    def addStudent(self):
        self.__studentFacade.addStudent()

    def updateStudent(self, array):
        self.__studentFacade.updateStudent(array)

    def getAllStudent(self):
        return self.__studentFacade.getAllStudent()

    def getAmount(self):
        return self.__studentFacade.getAmount()

    def getAllRooms(self):
        return self.__studentFacade.getAllRooms()