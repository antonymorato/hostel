from src.Inventory import Inventory
from src.Room import Room
from src.student import Student


class StudentFacade:
    def __init__(self, dict):
        self.__room = Room(dict["room_num"], dict["clean_rating"], dict["electrical_appliance"], dict["sex"])
        self.__inventory = Inventory(dict["inventory_name"], dict["name"], dict["surname"], dict["patronymic"],
                                     dict["amount"], dict["num_in_queue"])
        self.__student = Student(dict["name"], dict["surname"], dict["patronymic"], dict["bd"],
                                 dict["email"], dict["faculty"], dict["course"], dict["room_num"], dict["phone_number"],
                                 dict["sex"])

    def getStudentAmount(self):
        return self.__student.studentCount()

    def addStudent(self):
        # TODO write student to room
        stId = self.__student.addStudent()
        self.__room.addStudentToRoom(stId)

    def getRoom(self):
        self.__room.getRoom()

    def setRoom(self):
        self.__room.setRoom()

    # How did this occur here
    def getInventory(self):
        pass

    def getStudent(self):
        return self.__student.get()

    def updateStudent(self, array):
        self.__student.updateStudent()

    def removeStudent(self):
        self.__room.deleteStudentFromRoom(self.getStudent()["id"])
        self.__student.deleteStudent()

    def getAllRooms(self):
        rooms = self.__room.getAllRooms()
        res = []
        for room in rooms:
            temp = {"room_num": room['room'], "students": []}
            for i in room['students']:
                buff = self.__student.getStudentByID(i['stId'])
                temp["students"].append(buff["surname"] + " " + buff["name"] + " " + buff["patronymic"])
            res.append(temp)
        return res

    def getRoom(self):
        if self.__student.get()["room"] is not (None or ""):
            return self.__student.get()["room"]
        else:
            return "Not Found"

    def getAllStudent(self):
        return self.__student.getAllStudent()

    def getAmount(self):
        return self.__student.getAmount()
