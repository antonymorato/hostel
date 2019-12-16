from pymongo import MongoClient

from sqlConnect import sqlConn as sql

class mongoConnect(object):
	"""docstring for mongoConnect"""
	default=False
	maxSettlers=4
	def __init__(self, arg):
			pass
	@staticmethod
	def connect(ip,port):
		mongoConnect.conn = MongoClient("mongodb://{}:{}".format(ip,port))
		mongoConnect.db=mongoConnect.conn.hostel
		mongoConnect.collection=mongodb.db.rooms

	@staticmethod
	def updateRoom(room,pc=default,microwave=default,
		kettle=default,fridge=default):
		mongoConnect.collection=mongoConnect.db.rooms
		query={'number':room}
		new={'$set':{"pc":pc,
		'microwave':microwave,
		'fridge':fridge,'kettle':kettle}}
	# @staticmethod
	# def getStApplInfo(stId,room):
	# 	mongoConnect.collection.find_one({})
	@staticmethod
	def getRoomInfo(num):
		#returns dict
		return mongoConnect.collection.find_one({'number':num})
	@staticmethod
	def addStudent(stId,room,pc=default,fridge=default,
		microwave=default,kettle=default):
		#mongoConnect.collection=mongoConnect.db.rooms
		if mongoConnect.collection.find_one({'room':room,'students.stId'})!=None:
			
		if len(mongoConnect.collection.find_one({'room':room})['students'])<mongoConnect.maxSettlers:
			query={'room':room,'students.id':{'$ne':stId}}
			update={'$set':{'room':room},'$set':{'cleanRating':5},'$addToSet':{'students':{'stId':stId,'pc':pc,'fridge':fridge,
			'microwave':microwave,'kettle':kettle}}}
			mongoConnect.collection.update_one(query,update)
			return True
		else:
			return False
	@staticmethod
	def setCleanRating(room,rating):
		#options={'upsert':'false'}
		query={'room':room}
		update={'$set':{'cleanRating':rating}}
		mongoConnect.collection.update_one(query,update,upsert=True)
