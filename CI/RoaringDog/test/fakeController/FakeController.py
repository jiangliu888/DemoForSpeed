#!/usr/bin/python3
from flask import Flask, jsonify, request
import json
app = Flask("Controller")

POP_CPES = None
CPE_STATUS = {}

@app.route("/api/v1/ne/pop/<popId>/cpes", methods=['GET'])
def get_pop_cpes(popId):
    cpes = POP_CPES[popId]
    print("pop {} cpes {}".format(popId, cpes))
    return jsonify({"neId": int(popId),"cpes": cpes})

@app.route("/api/v1/ne/<neId>/homeCode", methods=['GET'])
def get_cpe_homeCode_status(neId):
    return jsonify({"homeCodes": [{"cac": 12, "eac": 11, "iface": "enp1s0f0", "index": 0}], "neId": neId})

@app.route("/api/v1/ne/homeCodes", methods=['GET'])
def get_cpe_homeCodes():
    ids = request.args.getlist('neId')
    res = []
    for neId in ids:
        if neId in CPE_HomeCodes.keys():
            res.append({"homeCodes": CPE_HomeCodes[neId], "neId": int(neId)})
        else:
            res.append({"homeCodes": [{"cac": -1, "eac": -1, "iface": "enp1s0f0", "index": 0}], "neId": int(neId)})
    return jsonify(res)

@app.route("/api/v1/ne/<neId>", methods=['GET'])
def get_cpe(neId):
    return CPE_STATUS[neId] if CPE_STATUS.has_key(neId) else "" 

@app.route("/api/v1/ne/<neId>", methods=['DELETE'])
def delete_cpe(neId):
    CPE_STATUS[neId] = "DELETED"

if __name__ == "__main__":
    import sys
    oureaPort = sys.argv[1] if sys.argv.__len__() > 1 else 6126
    try:
        with open("popCpes.json", "r") as popCpes_f:
            POP_CPES = json.load(popCpes_f)
        with open("homeCodes.json", "r") as homeCodes_f:
            CPE_HomeCodes = json.load(homeCodes_f)
        app.run(host="0.0.0.0", port=oureaPort, debug=False, threaded=True)
    except Exception as e:
        print(e)
