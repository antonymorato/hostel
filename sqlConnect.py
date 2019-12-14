import psycopg2
from psycopg2.extras import DictCursor


class sqlConn(object):
	"""docstring for sqlConn"""
	def __init__(self,dbname,user,password,host):
		self.dbname=dbname
		self.user=user
		self.password=password
		self.host=host
	def connect(self):
		self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, 
                        password=self.password,host=self.host)
		self.cursor = self.conn.cursor(cursor_factory=DictCursor)		
	def disconnect(self):
		self.cursor.close()
		self.conn.close()

	def getStudent(self,name='',surname='',patronymic=''):
		self.cursor.execute('''SELECT * FROM students WHERE
		 name = %(name)s or 
		 (name = %(name)s AND surname=%(surname)s) or 
		 (name = %(name)s AND surname=%(surname)s AND patronymic=%(patronymic)s)''',
		 {'name':name,'surname':surname,'patronymic':patronymic})

		return self.cursor.fetchall()
		#rows = self.cursor.fetchall()
		#students = {}
		#for row in rows:
 		#	students[row[0]] = [int(code) for code in row[1].split(',')]
		#self.conn.commit()
	#def setRoom():
		
	def setRoom(self,room,inventory,el_appliances):
		self.cursor.execute('')
	
	def setPenalty(self,name,surname,patronymic,addTime):
		self.cursor.execute('''UPDATE students SET work_min=work_min+addTime
		 WHERE name=%(name)s AND surname=%(surname)s AND patronymic=%(patronymic)s''',
			{'name':name,'surname':surname,'patronymic':patronymic})

	def prin(self):
		res=self.getStudent(name='John')
		print(res)
		print(type(res))
	def addStudent(self,Name,Surname,Patronymic,bd,mail,telephone,faculty,course,room):
		record=(Name,Surname,Patronymic,bd,mail,telephone,faculty,course,room)
		self.cursor.execute('INSERT INTO students (name,surname,patronymic,birth,email,phone,faculty,course,room) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) ',record)
		self.conn.commit()	
#TEST
def main():
	dbname='hostel'
	user='postgres'
	password='1663'
	host='localhost'
	test=sqlConn(dbname,user,password,host)
	test.connect()
	#test.addStudent('John','Snow','Batcovich','2000-08-14','smth@gmail.com','0992341563','IASA','3','404')
	print('yeap')
	test.prin()
	test.disconnect()

if __name__ == '__main__':
	main()