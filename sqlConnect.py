import psycopg2
from psycopg2.extras import DictCursor


class sqlConn(object):
	"""docstring for sqlConn"""
	def __init__(self,dbname,user,password,host):
		pass
	@staticmethod
	def connect(dbname,user,password,host,port):
		#sqlConn.conn = psycopg2.connect("dbname={} user={} password={} host={} port={}".format(dbname,user,password,host,port))
		sqlConn.conn = psycopg2.connect(dbname='hostel',user='postgres',password='1663',host='localhost')
		sqlConn.cursor = sqlConn.conn.cursor(cursor_factory=DictCursor)	
			
	
	@staticmethod
	def disconnect():
		sqlConn.cursor.close()
		sqlConn.conn.close()
	@staticmethod
	def getStudent(name='',surname='',patronymic=''):
		sqlConn.cursor.execute('''SELECT * FROM students WHERE
		 name = %(name)s or 
		 (name = %(name)s AND surname=%(surname)s) or 
		 (name = %(name)s AND surname=%(surname)s AND patronymic=%(patronymic)s)''',
		 {'name':name,'surname':surname,'patronymic':patronymic})

		for row in sqlConn.cursor:
			student={'firstname':row[1],'lastname':row[2],'patronymic':row[3],
			'birth':row[4],'email':row[5],'telephone':row[6],'faculty':row[7],'course':row[8],}
		#sqlConn.cursor.fetchall()
		return student
		#rows = self.cursor.fetchall()
		#students = {}
		#for row in rows:
 		#	students[row[0]] = [int(code) for code in row[1].split(',')]
		#self.conn.commit()
	#def setRoom():
	@staticmethod	
	def setRoom(room,inventory,el_appliances):
		#self.cursor.execute('')
		pass
	@staticmethod
	def setCleanRating(rating):
		sqlConn.cursor.execute('UPDATE rooms SET clean_rating = %(rate)s',{'rate':rating})
		sqlConn.conn.commit()
	@staticmethod
	def decreasePenalty(time):
		sqlConn.cursor.execute('UPDATE students SET work_min =work_min- %(time)s',{'time':time})
		sqlConn.conn.commit()
	@staticmethod
	def setPenalty(name,surname,patronymic,addTime):
		sqlConn.cursor.execute('''UPDATE students SET work_min=work_min+addTime
		 WHERE name=%(name)s AND surname=%(surname)s AND patronymic=%(patronymic)s''',
			{'name':name,'surname':surname,'patronymic':patronymic})
		sqlConn.conn.commit()
	@staticmethod
	def getPenalty(name='',surname='',patronymic=''):
		sqlConn.cursor.execute('''SELECT work_min FROM students 
		 WHERE name=%(name)s AND surname=%(surname)s AND patronymic=%(patronymic)s''',
			{'name':name,'surname':surname,'patronymic':patronymic})
		return sqlConn.cursor.fetchall()[0][0]
	@staticmethod
	def addStudent(Name,Surname,Patronymic,bd,mail,telephone,faculty,course,room,sex):
		record=(Name,Surname,Patronymic,bd,mail,telephone,faculty,course,room,sex)
		sqlConn.cursor.execute('INSERT INTO students (name,surname,patronymic,birth,email,phone,faculty,course,room,sex) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',record)
		sqlConn.conn.commit()

	@staticmethod
	def deleteStudent(name='',surname='',patronymic=''):
		sqlConn.cursor.execute('''DELETE * FROM students WHERE
		 name = %(name)s or 
		 (name = %(name)s AND surname=%(surname)s) or 
		 (name = %(name)s AND surname=%(surname)s AND patronymic=%(patronymic)s)''',
		 {'name':name,'surname':surname,'patronymic':patronymic})
		sqlConn.conn.commit()
	




#TEST

# def main():
# 	dbname='hostel'
# 	user='postgres'
# 	password='1663'
# 	host='localhost'
# 	sqlConn.connect(dbname,user,password,host,12314)
# 	r=sqlConn.getPenalty('John','Snow','Batcovich')	
# 	print(r)
# 	print(type(r))
# 	#test.addStudent('John','Snow','Batcovich','2000-08-14','smth@gmail.com','0992341563','IASA','3','404')
# 	print('yeap')
# 	#sqlConn.prin()
# 	r=sqlConn.getStudent(name='Denys')
# 	print(r)
# 	sqlConn.disconnect()

# if __name__ == '__main__':
# 	main()