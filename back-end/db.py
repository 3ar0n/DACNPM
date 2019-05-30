import pymysql.cursors  
 
# Kết nối vào database.
connection= None
def connectDB():
	global connection
	connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',                             
                            db='cnpm',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
	
	
             
def getData():
	sql = "SELECT * FROM `user`"
	cursor = connection.cursor()
	# Thực thi câu lệnh truy vấn (Execute Query).
	cursor.execute(sql)
	#return data
	return cursor
def getUser(_id):
	sql = "SELECT * FROM `user` WHERE user.id = '{0}'".format(_id) 
	cursor = connection.cursor()
	# Thực thi câu lệnh truy vấn (Execute Query).
	cursor.execute(sql)
	#return data
	return cursor
<<<<<<< HEAD
def insertData(_id, _password, _type):
	sql ="INSERT into `user`(id, mat_khau, account) values ('{0}','{1}','{2}')".format(_id,_password,_type)
	print("inserted !!!")
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
=======
def getUserByUsername(username):
	sql = "SELECT * FROM `user` WHERE user.tai_khoan = '{0}'".format(username) 
	cursor = connection.cursor()
	# Thực thi câu lệnh truy vấn (Execute Query).
	cursor.execute(sql)
	#return data
	return cursor
>>>>>>> 38a8ce6de7134140ae44f0f3623dbdbed5d5df8b
	
def closeDB():
	connection.close()
#if __name__ == "__main__":
#	connection = connectDB()
#	results = getUser(1);
#	for data in results:
#		print(data)
#	connectDB();