from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to check availability
@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return "hello world!", 200

# Endpoint to perform addition
@app.route('/calculator/add', methods=['POST'])
def add_numbers():
    data = request.json
    first = data.get("first")
    second = data.get("second")
    result = first + second
    return jsonify({"result": result}), 200

# Endpoint to perform subtraction
@app.route('/calculator/subtract', methods=['POST'])
def subtract_numbers():
    data = request.json
    first = data.get("first")
    second = data.get("second")
    result = first - second
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(debug=True)
