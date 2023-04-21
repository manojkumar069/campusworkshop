"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch130m8rddl13a53t3t0-a.oregon-postgres.render.com",
        database="todo_sh67",
        user="todo_sh67_user",
        password="IsyrEP4Fsjnj6PK3YVF1q8cBXqimnqYq")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
