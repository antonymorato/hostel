from src.DBConnect.mongoConnect import mongoConnect
from src.DBConnect.sqlConnect import sqlConn


class Room(object):
    def __init__(self, room_num, clean_rating=5,
                 electrical_appliance={"pc": False, "microwave": False, "fridge": False, "kettle": False}, sex="ч"):
        self.__sex = sex
        self.__room_num = room_num
        self.__clean_rating = clean_rating
        self.__electrical_appliance = electrical_appliance

    def getAllRooms(self):
        return mongoConnect.getAllRooms()

    def getRoom(self):
        return mongoConnect.getInfo(self.__room_num)

    def addStudentToRoom(self, stId):
        mongoConnect.addStudent(stId, self.__room_num, self.__electrical_appliance["pc"],
                                self.__electrical_appliance["fridge"], self.__electrical_appliance["microwave"],
                                self.__electrical_appliance["kettle"])

    def deleteStudentFromRoom(self,stId):
        mongoConnect.deleteStudent(stId,self.__room_num)