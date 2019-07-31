
#!/usr/bin/python
from flask import Flask, render_template
import os
import mysql.connector
import configparser
from secret import USER, PASSWORD

app = Flask(__name__)
DB_HOST = os.environ['MYSQL_HOST']
DB_PORT = os.environ['MYSQL_PORT']
CONFIG = configparser.RawConfigParser()


@app.route('/')
def hello():
    env = read_envkey()
    properties = read_properties()
    res = run_sql_statement()
    return render_template('index.html', env=env, properties=properties, res=res)

def read_properties():
    try:
        with open('/tmp/config.properties') as file:
            toret = [line.strip() for line in file]
        return toret
    except:
        return False
    #try:
    #    CONFIG.read('/tmp/config.properties')
    #    return CONFIG.get('testsection', 'testsection.testprop1')
    #except:
    #    return False


def read_envkey():
    try:
        return os.environ['ENVKEY']
    except:
        return False

def create_db_connection():
    mydb = mysql.connector.connect(
    user=USER,
    password=PASSWORD, 
    host=DB_HOST, 
    port=str(DB_PORT))
    return mydb

def run_sql_statement():
    try:
        mydb = create_db_connection()
    except:
        return False
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM cooper.`cooper-app`")
    res = mycursor.fetchall()
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
