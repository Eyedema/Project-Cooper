
#!/usr/bin/python
from flask import Flask, render_template
import os
import mysql.connector
from secret import USER, PASSWORD

app = Flask(__name__)

@app.route('/')
def hello():
    env = read_envkey()
    properties = read_properties()
    res = ''
    try:
        res = run_sql_statement()
        db_connected = True
    except:
        db_connected = False
    return render_template('index.html', env=env, properties=properties, res=res, db_connected=db_connected)

def read_properties():
    with open('config.properties') as file:
        toret = [line.strip() for line in file]
    return toret


def read_envkey():
    return os.environ['ENVKEY']

def create_db_connection():
    mydb = mysql.connector.connect(
    user=USER,
    password=PASSWORD, 
    host='mysql-cooper', 
    port='3307') # 3306 è giusta
    return mydb

def run_sql_statement():
    mydb = create_db_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM cooper.`cooper-app`")
    res = mycursor.fetchall()
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
