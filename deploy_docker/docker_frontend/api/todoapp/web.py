from flask import Flask
from api import backend_bp


app = Flask(__name__)

@app.route("/")
def index():
    return "Flask should not serve the static HTML pages. Make sure you adjust your setup!"

app.register_blueprint(backend_bp, url_prefix="/final")

if __name__ == "__main__":
    app.run(debug=True)
