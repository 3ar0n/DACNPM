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
	sql = "SELECT id, mat_khau FROM `user` WHERE user.id = '{0}'".format(id) 
	cursor = connection.cursor()
	cursor.execute(sql)
	return cursor.fetchone()

# lấy thông tin tháng mới nhất có chỉ số (tháng trước) của phòng trong bảng
def getLastMonth(_room):
	sql = "SELECT so_thang_o FROM `chi_so` WHERE ma_phong = '{0}' ORDER BY so_thang_o DESC".format(_room)
	cursor = connection.cursor()
	cursor.execute(sql)
	return cursor.fetchone()

# lấy thông tin mã biên lai mới nhất trong bảng
def getlastBillID():
	sql = "SELECT ma_bien_lai FROM `bien_lai` ORDER BY ma_bien_lai DESC"
	cursor = connection.cursor()
	cursor.execute(sql)
	return cursor.fetchone()

# thêm 1 biên lai mới cho 1 phòng
def addNewBill(_room):
	sql = "INSERT into `bien_lai`(ma_phong) values ('{0}')".format(_room)
	print("inserted !!!")
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()

# thêm các chỉ số điện, nước, tháng hiện tại theo mã biên lai và mã phòng
def addBillInfo(_room, _billID, _month, _csDien, _csNuoc):
	sql = "INSERT into `chi_so`(ma_phong, so_thang_o, cs_dien, cs_nuoc, ma_bien_lai) values ('{0}','{1}','{2}','{3}','{4}')".format(_room, _month, _csDien, _csNuoc, _billID)
	print("inserted !!!")
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()

# lấy chỉ số của tháng
def getIndexData(_room, _month):
	sql = "SELECT cs_dien, cs_nuoc FROM `chi_so` WHERE ma_phong = '{0}' and so_thang_o = '{1}'".format(_room, _month)
	cursor = connection.cursor()
	cursor.execute(sql)
	return cursor.fetchone()

# lấy giá điện, nước
def getPrice():
	sql = "SELECT * FROM `gia_tien`"
	cursor = connection.cursor()
	cursor.execute(sql)
	return cursor.fetchone()

# lấy giá phòng
def getRoomPrice(_room):
	sql = "SELECT gia_phong FROM `phongtro` WHERE ma_phong = '{0}'".format(_room)
	cursor = connection.cursor()
	cursor.execute(sql)
	return cursor.fetchone()

# cập nhật tổng tiền trọ, phụ thu vào biên lai
def updateBill(_billID, _total, _extra, _extraInfo):
	sql = "UPDATE `bien_lai` SET `tong_tien` = '{1}', `phu_phi` = '{2}', `mo_ta_phu_phi` = '{3}' WHERE `ma_bien_lai` = '{0}'".format(_billID, _total, _extra, _extraInfo)
	print("inserted !!!")
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
	
def closeDB():
	connection.close()

def getCustomerByRoomId(roomId):
	sql = "SELECT ten, sdt, cmnd FROM `khach_tro` WHERE khach_tro.phong_thue = '{0}' and khach_tro.tinh_trang=1".format(roomId)
	cursor = connection.cursor()
	cursor.execute(sql)
	return cursor.fetchall()

def getAllRooms():
	sql = "SELECT c.phong_thue as ma_phong, count(c.cmnd) as so_nguoi from khach_tro c group by c.phong_thue"
	cursor = connection.cursor()
	cursor.execute(sql)
	return cursor.fetchall()
#if __name__ == "__main__":
#	connection = connectDB()
#	results = getUser(1);
#	for data in results:
#		print(data)
#	connectDB();