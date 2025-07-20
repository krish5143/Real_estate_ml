from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import util

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/get_location_names", methods=["GET"])
def get_location_names():
    return jsonify({"locations": util.get_location_names()})


@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    location = data.get("location")
    sqft = data.get("sqft")
    bhk = data.get("bhk")
    bath = data.get("bath")

    if None in [location, sqft, bhk, bath]:
        return jsonify({"error": "Missing fields"}), 400

    estimated_price = util.get_estimated_price(
        location, float(sqft), int(bhk), int(bath)
    )
    return jsonify({"estimated_price": estimated_price})


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
