
from flask import Flask, request
from api.login import check_login

app = Flask(__name__)

@app.route("/api/v1/login", methods=["GET"])
def login():
    user = request.args.get('user')
    password = request.args.get('password')
    res = check_login(user, password)
    print(res)
    return res

@app.route("/")
def description():
    return "Nothing to see here."

def start():
    app.run()
