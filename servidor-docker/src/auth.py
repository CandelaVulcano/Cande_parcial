from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from flask import g
from dataclasses import dataclass

auth = HTTPBasicAuth()

@dataclass
class User:
    username: str
    password_hash: str

# Usuarios predefinidos para tus 6 amigos
users = {
    "amigo1": User(username="amigo1", password_hash=pwd_context.hash("clave1")),
    "amigo2": User(username="amigo2", password_hash=pwd_context.hash("clave2")),
    "amigo3": User(username="amigo3", password_hash=pwd_context.hash("clave3")),
    "amigo4": User(username="amigo4", password_hash=pwd_context.hash("clave4")),
    "amigo5": User(username="amigo5", password_hash=pwd_context.hash("clave5")),
    "amigo6": User(username="amigo6", password_hash=pwd_context.hash("clave6"))
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        user = users.get(username)
        if pwd_context.verify(password, user.password_hash):
            g.current_user = user
            return True
    return False