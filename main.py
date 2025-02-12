from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def index():
    fp = open("index.html", "r")
    return fp.read()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)