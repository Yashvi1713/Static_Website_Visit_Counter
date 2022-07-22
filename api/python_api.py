from flask import Flask, jsonify
import sqlite3
import os
from datetime import datetime
import requests

app = Flask(__name__)
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

@app.route('/counterIncrease/<string:ip>',methods=["GET"])
def hello_world(ip):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    database_location = os.path.join(THIS_FOLDER, 'database.db')
    database_connection = sqlite3.connect(database_location)
    database_cursor = database_connection.cursor()
    count = int(database_cursor.execute("SELECT count FROM visit").fetchone()[0])
    database_cursor.execute("UPDATE visit SET count = ? WHERE count = ?",(count+1,count))
    count = count + 1
    location_response = requests.get('https://ipapi.co/'+ip+'/json/').json()
    location_data = {
        "ip": ip,
        "city": location_response.get("city"),
        "region": location_response.get("region"),
        "country": location_response.get("country_name")
    }
    database_cursor.execute("INSERT into visitors VALUES (?,?,?,?,?)",(ip,now,location_response.get("city"),location_response.get("region"),location_response.get("country_name")))
    database_connection.commit()
    database_connection.close()
    message = {'count': count, 'location': location_data}
    response = jsonify(message)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
