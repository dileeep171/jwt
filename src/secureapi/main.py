# secureAPI
# First jwt did with using headers(adding gmail , password )( headers are in case senstive)
# 
# Actual JWT Stucture
# header = it stores the jwt toke
# Pay loader = actual data
# Signature = to verify the encryption


# from flask import Flask , request


# #  Old and first method
# app = Flask(__name__)

# database = [
#     {
#         "email": "nallavallidharm@gmail.com",
#         "password": "Dharm@123!@$"
#     }
# ]

# @app.route("/protect",methods = ["GET"])

# def handle_secure():
#   resEmail = request.headers.get("email")
#   resPass = request.headers.get("password")

#   items = list(filter(
#       lambda x: x["email"] == resEmail and x["password"] == resPass,
#       database
#   ))

#   if items:
#       return {
#           "status": "Password correct",
#           "email": resEmail
#       }

#   return {
#       "status": "Invalid"
#   }


from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import os
app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
jwt = JWTManager(app)

@app.route("/login", methods = ["POST"])
def login():
  username = request.json.get("username", None)
  password = request.json.get("password", None)
  if username != "dharma9770" or password != "Dharma@123":
    return jsonify({
      "msg" : "Bad username or password"
    }, 401 )
  access_token = create_access_token(identity = username)
  return jsonify(access_token)


@app.route("/protected",methods= ["GET"])
@jwt_required()
def protected():
  current_user = get_jwt_identity()
  return jsonify(logged_in_as=current_user), 200






if __name__ == "__main__":
  app.run(debug=True)
