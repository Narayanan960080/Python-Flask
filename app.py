from flask_mysqldb import MySQL
from flask import Flask,jsonify, request
from Main import MainData
from AccessControl import AccessControl



app = Flask(__name__)
mysql = MySQL(MainData.MySqlConnect(app))


@app.route('/createUsers',methods = ["POST"])
def addUser():
    try:
        data = request.get_json()
        result = AccessControl(mysql=mysql).createUser(data)
        return result
    except Exception as e:
        return jsonify({"Status":"0","Message":"Something issue please try later","error":e}) 
    

@app.route('/ListUsers')
def index():
    try:
        
        result = AccessControl(mysql=mysql).listUser()
        return result
    except Exception as e:
        print(e) 
        return jsonify({"status":"0","Message":"Something issue please try later"}) 


@app.route('/Login',methods = ["POST"])
def login():
    try:
        data = request.get_json()
        result = AccessControl(mysql=mysql).login(data)
        return result
    except Exception as e:
        print(e) 
        return jsonify({"status":"0","Message":"Something issue please try later"}) 



if __name__ == '__main__':
   app.run(debug=True)