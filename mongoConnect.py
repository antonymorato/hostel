from pymongo import MongoClient



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
		mongoConnect.collection=mongoConnect.db.rooms

	@staticmethod
	#TODO
	def updateRoom(room,pc=default,microwave=default,
		kettle=default,fridge=default):
		mongoConnect.collection=mongoConnect.db.rooms
		query={'number':room}
		new={'$set':{"pc":pc,
		'microwave':microwave,
		'fridge':fridge,'kettle':kettle}}
	

	@staticmethod
	def autorize(username,password):
		mongoConnect.collection=mongoConnect.db.users
		if mongoConnect.collection.find_one({'username':username,'password':password}):
			return True
		else:
			return False

	@staticmethod
	def deleteUser():
		mongoConnect.collection=mongoConnect.db.users
		mongoConnect.collection.delete_one({'username':username})

	@staticmethod
	def addUser(username,password):
		mongoConnect.collection=mongoConnect.db.users
		if mongoConnect.collection.find_one({'username':username})==None:
			mongoConnect.collection.insert_one({'username':username,'password':password})
			return True
		else:
			return False

	@staticmethod
	def getRoomInfo(num):
		#returns dict 
		return mongoConnect.collection.find_one({'number':num})
	@staticmethod
	def addStudent(stId,room,pc=default,fridge=default,
		microwave=default,kettle=default):
		#mongoConnect.collection=mongoConnect.db.rooms
		if mongoConnect.collection.find_one({'room':room})!=None:
				
			if len(mongoConnect.collection.find_one({'room':room})['students'])<mongoConnect.maxSettlers:
				if mongoConnect.collection.find_one({'room':room,'students.stId':stId})==None :
					query={'room':room,'students.id':{'$ne':stId}}
					update={'$set':{'room':room},'$set':{'cleanRating':5},'$addToSet':{'students':{'stId':stId,'pc':pc,'fridge':fridge,
					'microwave':microwave,'kettle':kettle}}}
					mongoConnect.collection.update_one(query,update)
					return True
			else:
				return False
		if mongoConnect.collection.find_one({'room':room})==None:
			mongoConnect.collection.insert_one({'room':room,'cleanRating':5,
						'students':[{'stId':stId,'pc':pc,'fridge':fridge,
						'microwave':microwave,'kettle':kettle}]})

			print('inserted')
			return True
		else:
			return False
			

	@staticmethod
	def setCleanRating(room,rating):
		#options={'upsert':'false'}
		query={'room':room}
		update={'$set':{'cleanRating':rating}}
		mongoConnect.collection.update_one(query,update,upsert=True)

	@staticmethod
	def getAllRooms():
		cursor= mongoConnect.db.rooms.find()
		return cursor

# mongoConnect.connect('localhost','27017')

# #r=mongoConnect.autorize('toha','123456789')
# #r=mongoConnect.addUser('toha','456789')

# r=mongoConnect.addStudent(stId=22,room='404')
# print(r)