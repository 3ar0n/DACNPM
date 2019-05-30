from flask import Flask,request,render_template
import db
import json
app = Flask(__name__)

# truy cập home
@app.route("/")
def hello():
	return render_template('layout.loitd',var1="ahihi")

@app.route("/users")
def findName():
	db.connectDB()
	results = db.getUser()
	temp =[]
	for data in results:
		temp.append(data)
	db.closeDB()
	return render_template('users.html', users=temp)
	#return json.dumps(temp)
	
@app.route("/user/<_cmnd>")
def findNameID(_cmnd):
	db.connectDB()
	results = db.getUserInfo(_cmnd);
	temp =[]
	for data in results:
		temp.append(data)
	db.closeDB()
	return render_template('user_info.html', user=temp[0])
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
	username = request.form['username']
	password = request.form['password']
	#print(request.data)
	users = db.getUser(username)
	db.closeDB()
	for user in users:
		if (user == None):
			return Response("{'a':'b'}", status=401, mimetype='application/json') 
		#encryptedPass = bcrypt.generate_password_hash(data.password)
		if (username == user['tai_khoan'] and password == user['mat_khau']):#bcrypt.check_password_hash(encryptedPass, password)):
			return user

	
