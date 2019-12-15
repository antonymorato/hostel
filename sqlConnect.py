import psycopg2
from psycopg2.extras import DictCursor


class sqlConn(object):
	"""docstring for sqlConn"""
	def __init__(self,dbname,user,password,host):
		pass
	@staticmethod
	def connect(dbname,user,password,host):
		sqlConn.conn = psycopg2.connect('''dbname={} user={}
		 password={} host={}
		  port={}''').format("hostel","postgres","1663","192.168.1.120","5432")
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

		return sqlConn.cursor.fetchall()
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
	@staticmethod
	def setPenalty(name,surname,patronymic,addTime):
		sqlConn.cursor.execute('''UPDATE students SET work_min=work_min+addTime
		 WHERE name=%(name)s AND surname=%(surname)s AND patronymic=%(patronymic)s''',
			{'name':name,'surname':surname,'patronymic':patronymic})
	@staticmethod
	def prin():
		res=sqlConn.getStudent(name='Denys')
		print(res)
		print(type(res))
	@staticmethod
	def addStudent(Name,Surname,Patronymic,bd,mail,telephone,faculty,course,room):
		record=(Name,Surname,Patronymic,bd,mail,telephone,faculty,course,room)
		sqlConn.cursor.execute('INSERT INTO students (name,surname,patronymic,birth,email,phone,faculty,course,room) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) ',record)
		sqlConn.conn.commit()	
	@staticmethod
	def deleteStudent(name='',surname='',patronymic=''):
		sqlConn.cursor.execute('''DELETE * FROM students WHERE
		 name = %(name)s or 
		 (name = %(name)s AND surname=%(surname)s) or 
		 (name = %(name)s AND surname=%(surname)s AND patronymic=%(patronymic)s)''',
		 {'name':name,'surname':surname,'patronymic':patronymic})
		




#TEST

def main():
	dbname='hostel'
	user='postgres'
	password='1663'
	host='localhost'
	sqlConn.connect(dbname,user,password,host)
	
	#test.addStudent('John','Snow','Batcovich','2000-08-14','smth@gmail.com','0992341563','IASA','3','404')
	print('yeap')
	sqlConn.prin()
	sqlConn.disconnect()

if __name__ == '__main__':
	main()