from src.DBConnect.mongoConnect import mongoConnect
from src.DBConnect.sqlConnect import sqlConn


class Student:
    def __init__(self, name=None, surname=None, patronymic=None, bd=None, email=None, faculty=None,
                 course=None, room_num=None, phone_number=None, sex=None,
                 electrical_appliance={"pc": False, "microwave": False, "fridge": False, "kettle": False}):
        self.__electrical_appliance = electrical_appliance
        self.__bd = bd
        self.__patronymic = patronymic
        self.__surname = surname
        self.__sex = sex
        self.__room_num = room_num
        self.__course = course
        self.__faculty = faculty
        self.__email = email
        self.__phone_number = phone_number
        self.__name = name

    def addStudent(self):
        try:
            sqlConn.addStudent(self.__name, self.__surname, self.__patronymic, self.__bd, self.__email, self.__phone_number,
                           self.__faculty, self.__course, self.__room_num, self.__sex)
            stId = sqlConn.getStudent(self.__name, self.__surname, self.__patronymic)["id"]
        # mongoConnect.addStudent(stId, self.__room_num, self.__electrical_appliance["pc"],
        #                         self.__electrical_appliance["fridge"], self.__electrical_appliance["microwave"],
        #                         self.__electrical_appliance["kettle"])
        except:
            return 1
        return stId

    def updateStudent(self, array):
        # array[0] містить початковий словник значень
        # аrray[1] містить словник даних якіпотрібно змінити за ключами словника йти в мейнІнтерфейс
        sqlConn.updateStudentInfo(array)

    def deleteStudent(self):
        sqlConn.deleteStudent(self.__name, self.__surname, self.__patronymic)

    def get(self):
        return sqlConn.getStudent(self.__name, self.__surname, self.__patronymic)

    def getCount(self):
        return sqlConn.studentCount()

    def getAllStudent(self):
        try:
            array = sqlConn.getAllStudents()
        except:
            buff = [{"name": "name", "surname": "surname", "patronymic": "patronymic", "bd": "bd",
                     "email": "email", "faculty": "faculty", "course": "course", "room_num": "room_num",
                     "phone_number": "phone_number", "sex": "sex", "clean_rating": "5",
                     "electrical_appliance": {"pc": False, "microwave": False, "fridge": False, "kettle": False},
                     "inventory_name": "Nothing",
                     "amount": "0", "num_in_queue": "0"}]
            return buff
        res = []
        for i in array:
            atrib = {}
            atrib["surname"] = i[1]
            atrib["name"] = i[2]
            atrib["patronymic"] = i[3]
            atrib["sex"] = i[11]
            atrib["room_num"] = i[9]
            atrib["faculty"] = i[7]
            atrib["course"] = i[8]
            atrib["phone_number"] = i[6]
            atrib["bd"] = i[4]
            atrib["email"] = i[5]
            atrib["clean_rating"] = "5"
            atrib["electrical_appliance"] = {"pc": False, "microwave": False, "fridge": False, "kettle": False}
            atrib["inventory_name"] = "Nothing"
            atrib["amount"] = "0"
            atrib["num_in_queue"] = "0"
            res.append(atrib)
        return res

    def getAmount(self):
        try:
            num = sqlConn.studentCount()
        except:
            return 100
        return num

    def getStudentByID(self, Id):
        return sqlConn.getSudentByID(Id)

    def __del__(self):
        self.__bd = None
        self.__patronymic = None
        self.__surname = None
        self.__sex = None
        self.__room_num = None
        self.__course = None
        self.__faculty = None
        self.__email = None
        self.__phone_number = None
        self.__address = None
        self.__name = None
