from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('layout.loitd',var1="ahihi")

@app.route("/user/<username>")
def findName(username):
	print ("The method: {0}".format(request.method))
	return "Hi {0}".format(username)