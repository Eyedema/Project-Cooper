
#!/usr/bin/python
from flask import Flask, render_template, request
import os
import mysql.connector
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
from secret import USER, PASSWORD

app = Flask(__name__)
try:
    DB_HOST = os.environ['MYSQL_HOST']
    DB_PORT = os.environ['MYSQL_PORT']
except:
    i = 1

CONFIG = configparser.RawConfigParser()


@app.route('/')
def hello():
    env = read_envkey()
    properties = read_properties()
    return render_template('index.html', env=env, properties=properties)

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

@app.route('/submit_query', methods=['POST'])
def run_sql_statement():
    try:
        mydb = create_db_connection()
    except:        
        return render_template('submit_query.html', error=True)
    query = request.form['query']
    mycursor = mydb.cursor()
    try:
        mycursor.execute(str(query)) # "SELECT * FROM cooper.`cooper-app`"
    except:
        return render_template('submit_query.html', syntaxerror=True)
    res = mycursor.fetchall()
    return render_template('submit_query.html', res=res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
