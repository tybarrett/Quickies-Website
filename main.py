from flask import Flask, send_file, request, redirect
import json

import mysql_wrapper

app = Flask(__name__)


@app.route("/")
def index():
    fp = open("1.html", "r")
    return fp.read()


@app.route("/<page_num>")
def specific_page(page_num):
    fp = open(f"{page_num}.html", "r")
    return fp.read()


@app.route("/get_msgs/<page_num>")
def get_msgs(page_num):
    msgs = mysql_wrapper.get_msgs(page_num)
    msgs = [list(x) for x in msgs]
    return json.dumps(msgs)


@app.route("/put_msg/<page_num>", methods=["GET", "POST"])
def put_msg(page_num):
    name = request.args.get("name")
    msg = request.args.get("chat_message")
    # page_num = request.form["page_num"]

    mysql_wrapper.put_msg({"name": name, "msg": msg, "page_num": page_num})
    return redirect("http://24.199.80.232/" + page_num, code=302)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)