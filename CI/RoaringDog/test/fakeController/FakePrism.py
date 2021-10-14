#!/usr/bin/python3
from flask import Flask, jsonify
import json
app = Flask("Prism")

ruleId = "5f9faf7fcc839dd262dc8b26"
groupId = "5f9fab9cd99ae5cab1bacc8f"

@app.route("/api/v1/mgr/rules", methods=['GET'])
def get_alert_rules():
    return jsonify({"id": ruleId}), 201

@app.route("/api/v1/mgr/groups", methods=['DELETE'])
def delete_group(groupId):
    print("delete group {}".format(groupId))
    return 204

@app.route("/api/v1/mgr/rules", methods=['DELETE'])
def delete_rule(rId):
    print("delete rule {}".format(rId))
    return 204


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=8000, debug=False, threaded=True)
    except Exception as e:
        print(e)
