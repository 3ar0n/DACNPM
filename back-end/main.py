from flask import Flask,request,render_template, Response
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
	
