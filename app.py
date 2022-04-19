# endpoint to return a list of users
# name, last name, email
from flask import Flask
from datetime import datetime, timedelta

import json
data = json.loads(open('users.json').read())

app = Flask(__name__)


def compute_age(string_birth_date:str):
    datetime_age = datetime.strptime(string_birth_date, "%Y-%m-%d")
    current_date = datetime.now()
    age = current_date.year - datetime_age.year - ((current_date.month, current_date.day) < (datetime_age.month, datetime_age.day))
    return f"The user is {age} years old."


@app.route('/users/<user_id>')
def get_users(user_id: int):
    user_id_parsed = int(user_id)
    if user_id_parsed <= len(data)-1:
        return data[user_id_parsed]
    else:
        return {"error":"Index out of range"}


@app.route('/age/<user_id>')
def get_user_age(user_id: int):
    user_id_parsed = int(user_id)
    if user_id_parsed <= len(data) - 1:
        return str(compute_age(data[user_id_parsed]['birth_date']))
    else:
        return {"error": "Index out of range"}


@app.route('/users/list')
def list_users():
    parsed_users_with_age = [{**x, 'age':compute_age(x['birth_date'])} for x in data]
    return {'users': parsed_users_with_age}