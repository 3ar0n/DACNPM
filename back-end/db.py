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
	
	
# lấy thông tin tất cả các user
def getData():
	sql = "SELECT * FROM `user`"
	cursor = connection.cursor()
	# Thực thi câu lệnh truy vấn (Execute Query).
	cursor.execute(sql)
	#return data
	return cursor

# lấy thông tin cơ bản của user theo id
def getUser(_id):
	sql = "SELECT * FROM `user` WHERE user.id = '{0}'".format(_id) 
	cursor = connection.cursor()
	cursor.execute(sql)
	return cursor

# lấy thông tin của khách trọ
def getUserInfo(_cmnd):
	sql = "SELECT ten, sdt, dia_chi, cmnd, nghe_nghiep, noi_lam_viec, phong_thue, DATE_FORMAT(ngay_thue, '%e/%m/%Y') as ngay_vao_o, tinh_trang FROM `khach_tro` WHERE khach_tro.cmnd = '{0}'".format(_cmnd)
	cursor = connection.cursor()
	cursor.execute(sql)
	return cursor

# thêm dữ liệu user vào bảng
def insertUser(_id, _password, _type):
	sql ="INSERT into `user`(id, mat_khau, account) values ('{0}','{1}','{2}')".format(_id,_password,_type)
	print("inserted !!!")
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()

# thêm thông tin khách trọ
def insertUserInfo(_id, _ten, _sdt, _diaChi, _ngheNghiep, _noiLamViec, _phong):
	sql ="INSERT into `khach_tro`(ten, sdt, dia_chi, cmnd, nghe_nghiep, noi_lam_viec, phong_thue, tinh_trang) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','1')".format(_id, _ten, _sdt, _diaChi, _ngheNghiep, _noiLamViec, _phong)
	print("inserted !!!")
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()

# thêm thông tin phương tiện của khách trọ
def insertUserVehicle(_id, _vCode, _vType):
	sql ="INSERT into `phuong_tien`(chu_xe, so_xe, loai_xe) values ('{0}','{1}','{2}')".format(_id, _vCode, _vType)
	print("inserted !!!")
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()

# thêm phòng trọ
def insertRoom(_room):
	sql ="INSERT into `phong_tro`(ma_phong) values ('{0}')".format(_room)
	print("inserted !!!")
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()

# thêm thông tin phòng trọ
def addRoomInfo(_room, _info):
	sql ="UPDATE TABLE `phong_tro` SET thong_tin = '{1}' WHERE ma_phong='{0}'".format(_room, _info)
	print("inserted !!!")
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()

# lấy thông tin cơ bản của user theo username (bị trùng với truy vấn phía trên)
def getUserById(id):
	sql = "SELECT id, mat_khau FROM `user` WHERE user.id = '{0}' and user.account_type=1".format(id) 
	cursor = connection.cursor()
	cursor.execute(sql)
	return cursor.fetchone()
	
def closeDB():
	connection.close()
#if __name__ == "__main__":
#	connection = connectDB()
#	results = getUser(1);
#	for data in results:
#		print(data)
#	connectDB();