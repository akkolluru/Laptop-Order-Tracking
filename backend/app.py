from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_database  # Import database connection
from kafka_producer import send_order_to_kafka
import datetime

app = Flask(__name__)
CORS(app)

# Get MongoDB connection
db = get_database()
orders_collection = db["orders"]

@app.route("/place_order", methods=["POST"])
def place_order():
    try:
        data = request.json
        order_id = "ORD" + str(int(datetime.datetime.utcnow().timestamp()))
        data["order_id"] = order_id
        data["order_date"] = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        # Store in MongoDB
        inserted_order = orders_collection.insert_one(data)
        data["_id"] = str(inserted_order.inserted_id)  # Convert ObjectId to string

        # Send to Kafka
        send_order_to_kafka(data)

        return jsonify({"message": "Order placed successfully!", "orderId": order_id, "_id": data["_id"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
