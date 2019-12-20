from src.DirectorFacade import DirectorFacade
from src.Work import Work


class Terminal:
    def __init__(self, field):
        self.__field = field

    def load_student(self, field):
        self.__dirFacade = DirectorFacade(self.__field)
        self.__dirFacade.addStudent()

    def update_student(self, dictin, array):
        self.__field = dictin
        self.__dirFacade = DirectorFacade(self.__field)
        self.__dirFacade.updateStudent(array)

    def search_student(self, dictin):
        self.__field = dictin
        self.__dirFacade = DirectorFacade(self.__field)
        return self.__dirFacade.getStudent(dictin)

    def delete_student(self, dictin):
        self.__field = dictin
        self.__dirFacade = DirectorFacade(self.__field)
        self.__dirFacade.removeStudent()

    def set_room(self, dictin):
        self.__field = dictin
        self.__dirFacade.setRoom(dictin)

    def get_total_students(self):
        self.__dirFacade = DirectorFacade(self.__field)
        n = self.__dirFacade.getAmount()
        if n == None:
            n = 100
        return n

    def get_total_free_places(self):
        pass

    def get_all_students(self):
        self.__dirFacade = DirectorFacade(self.__field)
        array = self.__dirFacade.getAllStudent()
        return array

    def get_rooms(self):
        self.__dirFacade = DirectorFacade(self.__field)
        rooms = self.__dirFacade.getAllRooms()
        res = [[] for i in range(5)]
        for room in rooms:
            if room["room_num"][0] == "1":
                res[0].append(room)
            if room["room_num"][0] == "2":
                res[1].append(room)
            if room["room_num"][0] == "3":
                res[2].append(room)
            if room["room_num"][0] == "4":
                res[3].append(room)
            if room["room_num"][0] == "5":
                res[4].append(room)
        return res

    def create_bill(self,dict):
        self.__dirFacade = DirectorFacade(self.__field)
        self.__dirFacade.createBill(dict)
