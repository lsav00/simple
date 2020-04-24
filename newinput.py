from flask import Flask
from flaskext.mysql import MySQL
app = Flask(__name__)

def getMysqlConnection():
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = "user_name"
    app.config['MYSQL_DATABASE_PASSWORD'] = "pass_string"
    app.config['MYSQL_DATABASE_DB'] = "db_name"
    app.config['MYSQL_DATABASE_HOST'] = "hostname"
    mysql.init_app(app)
    connection = mysql.connect()
    cursor = connection.cursor()
    return {"cursor":cursor,"connection":connection}


db =  getMysqlConnection()
cursor = db['cursor']
connection = db['connection']

def main_function():
    cursor.execute("Insert into table_name "
                       "(col1,col2,col3,col4) "
                       "Values (%s,%s,%s,%s,%s,%s)",
                       (val1,vla2,val3,val4)
                       )
    connection.commit()
    
