from abc import abstractmethod

from src.DBConnect.sqlConnect import sqlConn


class Work(object):
    def __init__(self):
        pass

    @abstractmethod
    def setWork(self):
        pass

    def addWork(self, field):
        if field["type"] is "Improvement":
            from src.ImprovementWork import ImprovementWork
            impWork = ImprovementWork(field["name"], field["surname"], field["patronymic"], field["Time"])
            impWork.setWork()
            del impWork
        else:
            from src.PenaltyWork import PenaltyWork
            penWork = PenaltyWork(field["name"], field["surname"], field["patronymic"], field["Time"])
            penWork.setWork()
            del penWork

    def decreaseWork(self, field):
        impWork = ImprovementWork(field["name"], field["surname"], field["patronymic"], field["Time"])
        impWork.setWork()

    def getWork(self, field):
        if field["type"] is "Improvement":
            from src.ImprovementWork import ImprovementWork
            impWork = ImprovementWork(field["name"], field["surname"], field["patronymic"], field["Time"])
            return impWork.getWork()

        else:
            from src.PenaltyWork import PenaltyWork
            penWork = PenaltyWork(field["name"], field["surname"], field["patronymic"], field["Time"])
            return penWork.getPenalty()


class ImprovementWork(Work):
    def __init__(self, name, surname, patronymic, time):
        self.__time = time
        self.__patronymic = patronymic
        self.__surname = surname
        self.__name = name

    def setWork(self):
        sqlConn.addPenalty(self.__name, self.__surname, self.__patronymic, self.__time)

    def decreaseWork(self):
        sqlConn.decreasePenalty(self.__time, self.__name, self.__surname, self.__patronymic, self.__addTime)

    def getWork(self):
        return sqlConn.getPenalty(self.__name, self.__surname, self.__patronymic)


class PenaltyWork(Work):
    def __init__(self, name, surname, patronymic, time):
        self.__time = time
        self.__patronymic = patronymic
        self.__surname = surname
        self.__name = name

    def setWork(self):
        sqlConn.addPenalty(self.__name, self.__surname, self.__patronymic, self.__time)

    def decreaseWork(self):
        sqlConn.decreasePenalty(self.__time, self.__name, self.__surname, self.__patronymic, self.__addTime)

    def getPenalty(self):
        return sqlConn.getPenalty(self.__name, self.__surname, self.__patronymic)