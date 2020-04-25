#!/usr/bin/python


from flaskext.mysql import MySQL
from flask import Flask, render_template, request


app = Flask(__name__)


app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'larry'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'fire'

mysql = MySQL()
mysql.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
	rendr=render_template('index.html')
	connection=mysql.connect()
	if request.method == "POST":
		details = request.form
		firstName = details['fname']
		lastName = details['lname']
		cur = connection.cursor()
		cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
		connection.commit()
		cur.close()
		return rendr
	
	#return rendr


if __name__ == '__main__':
	app.run()
