from flask import session
def login_user(Usuario):
    session["id"]=Usuario.id
    session["username"]=Usuario.username
    session["admin"]=Usuario.admin
def logout_user():
    session.pop("id", None)
    session.pop("username", None)
    session.pop("admin", None)
