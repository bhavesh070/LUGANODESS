from flask import Flask, request, jsonify

app = Flask(__name__)

heimdall_height = 0
bor_height = 0

@app.route('/update', methods=['POST'])
def update_heights():
    global heimdall_height, bor_height
    data = request.get_json()
    heimdall_height = data.get('heimdall_height', heimdall_height)
    bor_height = data.get('bor_height', bor_height)

    return jsonify({"message": "Heights updated", "heimdall_height": heimdall_height, "bor_height": bor_height})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)