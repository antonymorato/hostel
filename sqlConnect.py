import psycopg2
from psycopg2.extras import DictCursor


class sqlConn(object):
	"""docstring for sqlConn"""
	def __init__(self,dbname,user,password,host):
		pass
	@staticmethod
	def connect(dbname,user,password,host,port):
		sqlConn.conn = psycopg2.connect("dbname={} user={} password={} host={} port={}".format(dbname,user,password,host,port))
		#sqlConn.conn = psycopg2.connect(dbname='hostel',user='postgres',password='1663',host='localhost')
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
			'birth':row[4],'email':row[5],'telephone':row[6],'faculty':row[7],'course':row[8],'room':row[9],'sex':row[11]}
		
		return student
		
	
	@staticmethod
	def setCleanRating(rating):
		sqlConn.cursor.execute('UPDATE rooms SET clean_rating = %(rate)s',{'rate':rating})
		sqlConn.conn.commit()
	@staticmethod
	def decreasePenalty(time,name='',surname='',patronymic=''):
		sqlConn.cursor.execute('''UPDATE students SET work_min =work_min- %(time)s WHERE
			name = %(name)s or 
		 (name = %(name)s AND surname=%(surname)s) or 
		 (name = %(name)s AND surname=%(surname)s AND patronymic=%(patronymic)s)''',
		 {'name':name,'surname':surname,'patronymic':patronymic})
		sqlConn.conn.commit()
	@staticmethod
	def addPenalty(name,surname,patronymic,addTime):
		sqlConn.cursor.execute('''UPDATE students SET work_min=work_min+%(addTime)s
		 WHEREname = %(name)s or 
		 (name = %(name)s AND surname=%(surname)s) or 
		 (name = %(name)s AND surname=%(surname)s AND patronymic=%(patronymic)s)''',
		 {'name':name,'surname':surname,'patronymic':patronymic,'addTime':addTime})
		sqlConn.conn.commit()
	@staticmethod
	def getPenalty(name='',surname='',patronymic=''):
		sqlConn.cursor.execute('''SELECT work_min FROM students 
		 WHERE name = %(name)s or 
		 (name = %(name)s AND surname=%(surname)s) or 
		 (name = %(name)s AND surname=%(surname)s AND patronymic=%(patronymic)s)''',
		 {'name':name,'surname':surname,'patronymic':patronymic})
		return sqlConn.cursor.fetchall()[0][0]
	@staticmethod
	def addStudent(Name,Surname,Patronymic,bd,mail,telephone,faculty,course,room,sex):
		record=(Name,Surname,Patronymic,bd,mail,telephone,faculty,course,room,sex)
		sqlConn.cursor.execute('INSERT INTO students (name,surname,patronymic,birth,email,phone,faculty,course,room,sex) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',record)
		sqlConn.conn.commit()
		sqlConn.cursor.fetchall()

	@staticmethod
	def deleteStudent(name='',surname='',patronymic=''):
		sqlConn.cursor.execute('''DELETE * FROM students WHERE
		 name = %(name)s or 
		 (name = %(name)s AND surname=%(surname)s) or 
		 (name = %(name)s AND surname=%(surname)s AND patronymic=%(patronymic)s)''',
		 {'name':name,'surname':surname,'patronymic':patronymic})
		sqlConn.conn.commit()
	
	@staticmethod
	def studentCount():
		sqlConn.cursor.execute('SELECT COUNT(*) FROM students')
		return sqlConn.cursor.fetchone()[0] 
	@staticmethod
	def getAllStudents():
		sqlConn.cursor.execute('SELECT * FROM students ORDER BY surname ASC')


