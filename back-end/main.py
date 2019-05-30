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
	results = db.getData();
	temp =[]
	for data in results:
		temp.append(data)
	db.closeDB()
	return json.dumps(temp)
@app.route("/user/<int:username>")
def findNameID(username):
	db.connectDB()
	results = db.getUser(username);
	temp =[]
	for data in results:
		temp.append(data)
	db.closeDB()
	return json.dumps(temp)

@app.route("/insert")
def insertDB():
	db.connectDB()
	db.insertData("5","123456","huan")
	db.closeDB()
	return 200;
