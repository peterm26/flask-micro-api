from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route("/data", methods=["GET", "POST"])
def data():
    sample_data = {
        "course": "Flask Micro-API",
        "topics": ["routes", "JSON", "testing"],
    }

    if request.method == "POST":
        submitted_data = request.get_json(silent=True)

        if submitted_data is None:
            return jsonify({"error": "Please send valid JSON data."}), 400

        return jsonify({
            "message": "Data received successfully,",
            "received": submitted_data,
        }), 201

    return jsonify(sample_data), 200

if __name__ == "__main__":
    app.run(debug=True)

