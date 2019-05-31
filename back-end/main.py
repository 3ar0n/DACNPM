from flask import Flask,request,render_template, Response
import db
import json
app = Flask(__name__)
	
@app.route("/user/<_cmnd>")
def findNameID(_cmnd):
	db.connectDB()
	results = db.getUserInfo(_cmnd);
	temp =[]
	for data in results:
		temp.append(data)
	db.closeDB()
	return json.dumps(user=temp[0])
	#return json.dumps(temp)

@app.route("/insert")
def insertDB():
	db.connectDB()
	_id = "test1235"
	db.insertData(_id, "1234567", 0)
	db.closeDB()
	return "OK"

@app.route("/login", methods=['POST'])
def login():
	db.connectDB()
	#data = request.form
	id = request.form['id']
	password = request.form['mat_khau']
	#print(request.data)
	user = db.getUserById(id)
	db.closeDB()
	if (user == None):
		return Response(False, status=401, mimetype='application/json')
	if (id == user['id'] and password == user['mat_khau']):
		return Response(True, status=200, mimetype='application/json')
	return Response(False, status=401, mimetype='application/json')

# input: mã phòng, chỉ số điện mới, chỉ số nước mới, tiền phụ thu, mô tả phụ thu
# output: none (dữ liệu được ghi vào trong bảng) "OK" nếu thành công
@app.route("/test_them_chi_so")
def newBill():
	db.connectDB()
	#_room = request.form['ma_phong']
	_room = "A001"							# lấy thông tin phòng
	results = db.getLastMonth(_room)		# lấy tháng trước của phòng trong bảng chi_so
	_lastMonth = results['so_thang_o']
	_curMonth = _lastMonth + 1				# tháng hiện tại (biên lai mới)
	
	db.addNewBill(_room)					# tạo biên lai mới cho phòng trong bảng bien_lai
	results = db.getlastBillID()			# lấy mã biên lai vừa mới tạo
	_lastBillID = int(results['ma_bien_lai'])
	
	#_cs_dien = request.form['cs_dien']
	#_cs_nuoc = request.form['cs_nuoc']
	_cs_dien = 100
	_cs_nuoc = 10
	db.addBillInfo(_room,_lastBillID,_curMonth,_cs_dien,_cs_nuoc)	# thêm các chỉ sôs trong biên lai tháng hiện tại

	# tính tiền phòng
	results = db.getRoomPrice(_room)
	tien_co_ban = results['gia_phong']		# giá phòng (từ bảng phong_tro)

	#tien_phu_thu = request.form['phu_thu']
	#thong_tin_phu_thu = request.form['mo_ta']
	tien_phu_thu = 50000					# tiền phụ thu
	thong_tin_phu_thu = "bóng đèn"			# thông tin phụ thu
	
	results = db.getIndexData(_room, _lastMonth)
	_cs_dien_old = results['cs_dien']
	_cs_nuoc_old = results['cs_nuoc']

	# trên thực tế _cs_dien_new === _cs_dien
	results = db.getIndexData(_room, _curMonth)
	_cs_dien_new = results['cs_dien']
	_cs_nuoc_new = results['cs_nuoc']
	
	results = db.getPrice()
	_gia_dien = results['gia_dien']
	_gia_nuoc = results['gia_nuoc']
	
	tong_tien = tien_co_ban + tien_phu_thu + _gia_dien * (_cs_dien_new - _cs_dien_old) + _gia_nuoc * (_cs_nuoc_new - _cs_nuoc_old)
	db.updateBill(_lastBillID, tong_tien, tien_phu_thu, thong_tin_phu_thu)
	db.closeDB()
	return "OK"

@app.route("/customerinroom/<roomid>")
def getcustomer(roomid):
	db.connectDB()
	return json.dumps(db.getCustomerByRoomId(roomid))

@app.route("/rooms")
def getRooms():
	db.connectDB()
	return json.dumps(db.getAllRooms())
