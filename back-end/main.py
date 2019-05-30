from flask import Flask,request,render_template
import db
import json
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('layout.loitd',var1="ahihi")

@app.route("/users")
def findName():
	db.connectDB()
	results = db.getData()
	temp =[]
	for data in results:
		temp.append(data)
	db.closeDB()
	return render_template('users.html', users=temp)
	#return json.dumps(temp)
	
@app.route("/user/<_username>")
def findNameID(_username):
	db.connectDB()
	results = db.getUser(_username);
	temp =[]
	for data in results:
		temp.append(data)
	db.closeDB()
	return json.dumps(temp)

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
	users = db.getUserByUsername(username)
	db.closeDB()
	for user in users:
		if (user == None):
			return Response("{'a':'b'}", status=401, mimetype='application/json') 
		#encryptedPass = bcrypt.generate_password_hash(data.password)
		if (username == user['tai_khoan'] and password == user['mat_khau']):#bcrypt.check_password_hash(encryptedPass, password)):
			return user

	
