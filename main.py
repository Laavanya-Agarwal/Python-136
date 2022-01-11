from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

#to get all of the data
@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "Success!"
    }), 200

#to get only one of the planet's data
@app.route("/planet")
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item ["name"]==name)
    return jsonify({
        "data": planet_data,
        "message": "Success!"
    }), 200
#to find specific planet information, type http://127.0.0.1:5000/planet?name= and then enter name

if __name__ == "__main__":
    app.run()