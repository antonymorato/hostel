from __future__ import annotations
from src import Work
from src.DBConnect.sqlConnect import sqlConn


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