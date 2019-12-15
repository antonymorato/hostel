from pymongo import MongoClient


from pprint import pprint
class mongoConnect(object):
	"""docstring for mongoConnect"""
	default=False
	def __init__(self, arg):
		super(mongoConnect, self).__init__()
		self.arg = arg
	@staticmethod
	def connect(ip,port):
		mongoConnect.conn = MongoClient("mongodb://{}:{}".format(ip,port))
		mongoConnect.db=mongoConnect.conn.hostel
	@staticmethod
	def setRoom(room,pc=default,microwave=default,
		kettle=default,fridge=default):
		mongoConnect.collection=mongoConnect.db.rooms
		
		record={"number":room,"pc":pc,
		'microwave':microwave,'fridge':fridge,'kettle':kettle}
		mongoConnect.collection.insert_one(record)
	@staticmethod
	def getInfo(num):
		return mongoConnect.db.rooms.find_one({'number':num})


ip='localhost'
port='27017'
mongoConnect.connect(ip,port)
mongoConnect.setRoom(403,fridge=True)

res=mongoConnect.getInfo(403)
print(type(res))
print(res['pc'])
