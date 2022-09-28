import time
from flask_mysqldb import MySQL
from flask import Flask,jsonify, request
from Config import Config
from AccessControl import AccessControl
import threading



app = Flask(__name__)
mysql = MySQL(Config.MySqlConnect(app))



def task():
    print('task started...')
    print(threading.current_thread().name)
    time.sleep(60)
    print("completed")
    

@app.route('/createUsers',methods = ["POST"])
def addUser():
    try:
        data = request.get_json()
        result = AccessControl(mysql=mysql).createUser(data)
        return result
    except Exception as e:
        return jsonify({"Status":"0","Message":"Something issue please try later","error":e}) 
    

@app.route('/ListUsers',methods = ["POST","GET"])
def index():
    threading.Thread(target=task).start()
    # task()
    try:
        data = request.get_json()
        result = AccessControl(mysql=mysql).listUser(data)
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



@app.route('/Testing')
def testing():
     return jsonify({"Status":"1","Message":"Server Run Successfully"})


if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0',port=8080)