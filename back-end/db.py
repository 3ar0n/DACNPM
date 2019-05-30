import pymysql.cursors  
 
# Kết nối vào database.
connection= None
def connectDB():
	global connection
	connection = pymysql.connect(host='localhost',
                            user='root',
                            password='123456',                             
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
def getUser(id):
	sql = "SELECT * FROM `user` WHERE user.id = {0}".format(id) 
	cursor = connection.cursor()
	# Thực thi câu lệnh truy vấn (Execute Query).
	cursor.execute(sql)
	#return data
	return cursor
def getUserByUsername(username):
	sql = "SELECT * FROM `user` WHERE user.tai_khoan = '{0}'".format(username) 
	cursor = connection.cursor()
	# Thực thi câu lệnh truy vấn (Execute Query).
	cursor.execute(sql)
	#return data
	return cursor
def insertData(_id,mat_khau,tai_khoan):
	sql ="INSERT into `user`(id, mat_khau, tai_khoan) values ({0},{1},{2})".format(_id,mat_khau,tai_khoan)
	print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
def closeDB():
	connection.close()
#if __name__ == "__main__":
#	connection = connectDB()
#	results = getUser(1);
#	for data in results:
#		print(data)
#	connectDB();