#!/usr/bin/python3
from flask import Flask, jsonify,request
import json
app = Flask(__name__)
ticket = None


@app.route("/api/v2/app/6099029b1841180008a340e7/entry/609d0ff49f3acd00084850c7/data", methods=['POST'])
def get_ticket():
    return jsonify(ticket)


if __name__ == "__main__":
    try:
        with open("ticketMesg.json", "r", encoding='utf-8') as ticket_f:
            ticket = json.load(ticket_f)
            print(type(ticket))
        app.run(host="0.0.0.0", port=443, debug=True, threaded=True, ssl_context='adhoc')
    except Exception as e:
        print(e)