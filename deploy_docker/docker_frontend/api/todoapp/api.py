import urllib.request
import urllib.parse
import datetime
import re
from io import BytesIO
from flask import Blueprint, jsonify, send_file

backend_bp = Blueprint("backend", __name__)

@backend_bp.route("/")
def info():
    values = get_data()
    if not values["success"]:
        return jsonify(values), 500

    return jsonify({"message": "Welcome to the backend. Use /final/json or /final/image to check the API output."})

def get_data(filename="info.txt"):
    data = {
        "success": False
    }
    try:
        with open(filename, "r") as fp:
            lines = fp.readlines()
    except FileNotFoundError:
        data.update(msg=f"{filename} was not found.")
        return data
    except IsADirectoryError:
        data.update(msg=f"{filename} is a directory and should be a file.")
        return data

    if len(lines) < 2:
        data.update(msg=f"The contents of {filename} are incorrect.")
        return data
    
    name = lines[0].strip()
    website = lines[1].strip()
    # website_matches = re.match("A\d{8}", website)

    if not name:
        data.update(msg=f"The contents of {filename} are incorrect.")
        return data

    data.update(success=True)
    data.update(user_website=website, user_name=name)
    return data

@backend_bp.route("/json")
def display():
    values = get_data()

    if not values["success"]:
        return jsonify(values), 500

    return jsonify(values)

@backend_bp.route("/image")
def qrcode():
    values = get_data()

    if not values["success"]:
        return jsonify(values), 500

    name = values["user_name"]
    website = values["user_website"]

    cur_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    url = "https://api.qrserver.com/v1/create-qr-code/?"
    params = {
        "size": "200x200",
        "data": "\n".join([name, website, cur_date]),
        "format": "png",
    }

    url += urllib.parse.urlencode(params)

    with urllib.request.urlopen(url) as response:
        image = response.read()

    return send_file(BytesIO(image), mimetype="image/png")

