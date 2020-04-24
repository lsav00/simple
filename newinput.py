from flask import Flask
from flaskext.mysql import MySQL
app = Flask(__name__)

def getMysqlConnection():
	mysql = MySQL()
	app.config['MYSQL_DATABASE_HOST'] = 'localhost'
	app.config['MYSQL_DATABASE_USER'] = 'larry'
	app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
	app.config['MYSQL_DATABASE_DB'] = 'fire'
	mysql.init_app(app)
	connection = mysql.connect()
	cursor = connection.cursor()
	return {"cursor":cursor,"connection":connection}


db =  getMysqlConnection()
cursor = db['cursor']
connection = db['connection']

def main_function():
	cursor.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
	connection.commit()
