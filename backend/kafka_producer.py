from kafka import KafkaProducer
import json

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_order_to_kafka(order_data):
    """ Sends order data to Kafka topic """
    producer.send("orders", order_data)
    producer.flush()
    print(f"✅ Order sent to Kafka: {order_data}")

# Test sending an order
if __name__ == "__main__":
    sample_order = {
        "order_id": "ORD12345",
        "customer_id": "CUST5678",
        "laptop_model": "Model A",
        "amount": 1200,
        "order_date": "2025-02-17",
        "status": "Pending"
    }
    send_order_to_kafka(sample_order)
