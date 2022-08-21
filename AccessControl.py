from flask import jsonify, request
from token_genretor import PasswordSecurity
from token_genretor import TokenGenretor
import bcrypt


class AccessControl:
    def __init__(self,mysql):
        self.mysql = mysql
        
    def createUser(self,data):
        try:
            name = data['name']
            mail =data['mail']
            mobile = data['mobile']
            password = data['password'].encode('utf-8')
            passw = PasswordSecurity.encryptPassword(password)
            cur = self.mysql.connection.cursor()
            isNewUser ='''SELECT * FROM users WHERE EMAIL = %s'''
            cur.execute(isNewUser,[mail])
            self.mysql.connection.commit()
            control = cur.fetchone()
            if control:
                return jsonify({"Status":"0","Message":"User Mail Already existed"})
            else:    
                sql = "insert into users(USERNAME,MOBILENO,EMAIL,PASSWORD) values (%s,%s,%s,%s)"
                cur.execute(sql,[name,mobile,mail,passw])
                self.mysql.connection.commit()
                
                return jsonify({"Status":"1","Message":"user created Succesfully"})

        except Exception as e:
            print(e) 
            return jsonify({"Status":"0","Message":"Something issue please try later"}) 
        finally:
            cur.close()

    def listUser(self):
        cur = self.mysql.connection.cursor()
        try:
            cur.execute('''SELECT * FROM users''')
            row = cur.fetchall()
            payload = []
            content = {}
            if row:
                for result in row:    
                    content = {'id': result[0], 'username': result[1], 'Email': result[3],'mobile':result[2],'password':result[4]}
                    payload.append(content)
                    content = {}
                return jsonify({"Status":"1","message":"Data Fetched Successfully","listOfUser":payload})
            else:
                return jsonify({"Status":"1","message":"No Data Available"}) 
        except Exception as e:
            print(e) 
            jsonify({"Status":"0","Message":"Something issue please try later"}) 
        finally:
            cur.close()



    def login(self,json_data):
        try:
            username = json_data["username"]
            passwordData = json_data["password"].encode("utf-8")
            cur = self.mysql.connection.cursor()
            query ='''SELECT * FROM users WHERE EMAIL = %s'''
            cur.execute(query,[username])
            self.mysql.connection.commit()
            control = cur.fetchone()
            if control:
                hased_KEY = control[4].encode("utf-8")
                if bcrypt.checkpw(password=passwordData,hashed_password=hased_KEY):
                    token = TokenGenretor(control[1],control[2]).encodeToken()
                    return jsonify({"Status":"1","message":"Data Fetched Successfully","token":token})
                else:
                    return jsonify({"Status":"1","message":"Incorrect username or Password!"})    
            else:
                return jsonify({"Status":"1","message":"This mail Not Registered"})  
              
        except Exception as e:
            print(e)
            return jsonify({"Status":"0","Message":"Something issue please try later"})  

        finally:
            cur.close()

