#!/usr/bin/python


import mysql.connector
mydb=mysql.connector.connect( host="localhost", user="larry", passwd="password", database="fire")
print(mydb) 

mycursor= mydb.cursor()
mycursor.execute("select saybye from greetings")
myresult=mycursor.fetchall()

from flask import Flask, render_template
app=Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("index.html") 
if __name__== "__main__":
	app.run()

