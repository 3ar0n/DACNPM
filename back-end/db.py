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

def getUserInfo(_cmnd):
	sql = "SELECT ten, sdt, dia_chi, cmnd, nghe_nghiep, noi_lam_viec, phong_thue, DATE_FORMAT(ngay_thue, '%e/%m/%Y') as ngay_vao_o, tinh_trang FROM `khach_tro` WHERE khach_tro.cmnd = '{0}'".format(_cmnd)
	cursor = connection.cursor()
	# Thực thi câu lệnh truy vấn (Execute Query).
	cursor.execute(sql)
	#return data
	return cursor

def insertData(_id, _password, _type):
	sql ="INSERT into `user`(id, mat_khau, account) values ('{0}','{1}','{2}')".format(_id,_password,_type)
	print("inserted !!!")
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
def getUserByUsername(username):
	sql = "SELECT * FROM `user` WHERE user.tai_khoan = '{0}'".format(username) 
	cursor = connection.cursor()
	# Thực thi câu lệnh truy vấn (Execute Query).
	cursor.execute(sql)
	#return data
	return cursor
	
def closeDB():
	connection.close()
#if __name__ == "__main__":
#	connection = connectDB()
#	results = getUser(1);
#	for data in results:
#		print(data)
#	connectDB();