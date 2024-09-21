
from os.path import exists
from json import loads

def check_login(user, password):
    organization = user.split("@")[1]
    user_short = user.split("@")[0]
    if not exists(f"data/orgs/{organization}"):
        return {"status": "error", "message": "User or password incorrect."}
    with open(f"data/orgs/{organization}/users.json") as file:
        users = loads(file.read())
    if user_short not in users:
        return {"status": "error", "message": "User or password incorrect."}
    if users[user_short]["password"] != password:
        return {"status": "error", "message": "User or password incorrect."}
    return {"status": "success", "message": "Login successful."}