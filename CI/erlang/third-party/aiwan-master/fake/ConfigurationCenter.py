from flask import Flask, jsonify, request

app = Flask("sn")

AUTH_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VJZCI6Ik9wZW5XcnQiLCJleHAiOjE1OTQ2NzE2MTgsImlhdCI6MTU5NDY2ODAxOH0.BkEq0Ep6wgBFgUXUtBKFNQUKhAq9ePwXdbb6RlKHtLXh2jEwrfK_mTLyBu88O74PuYekOejFR1SZF-liIS08TetF-aHG9srH_SIXde4nlV4HWvfwi7fohemGxdYteXVIAhcswmhKNyQSxEM2X-RYRuocTCUqH_VKM7j-J7tKcwY"


@app.route("/api/v2/snTransferNEId/<sn>", methods=['GET'])
def get_ne_id(sn):
    token = request.headers.get('Authorization')
    if not token or AUTH_TOKEN not in token:
        return "Unauthorized", 401
    otherModeCpeList = {"4280": 17026, "4290": 17043, "4270": 17009}
    neId = int(sn, 16) if str(sn) not in otherModeCpeList.keys() else otherModeCpeList[str(sn)]
    print("sn to neId {} -> {}".format(sn, neId))
    return jsonify({"neIds": [int(neId)]})


@app.route("/api/v1/tokens", methods=['POST'])
def get_tokens():
    return jsonify({"token": AUTH_TOKEN, "expiresIn": 234414})


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=7001, debug=False, threaded=True)
    except Exception as e:
        print(e)
