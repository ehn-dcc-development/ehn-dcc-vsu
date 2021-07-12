from datetime import datetime

from flask import (
    Flask,
    render_template,
    send_file,
    url_for
)

app = Flask(__name__)


# TODO: timer to run zlib compression on JSON files in static to generate a new value-set.zip every N seconds

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/vsc_most_recent", methods=["GET"])
def vsu_most_recent():
    return str(datetime.utcnow())    # TODO: update with simulated "data set" upload


@app.route("/value-set", methods=["GET"])
def vsu():
    return send_file(url_for("static", "value-set.zip"), mimetype="application/x-zip-compressed")
