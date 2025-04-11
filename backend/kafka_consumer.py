from kafka import KafkaConsumer
from database import get_database
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Connect to MongoDB
db = get_database()
orders_collection = db["orders"]

# Mailtrap credentials
SMTP_HOST = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 587
SMTP_USER = "c7fe23c029adf1"
SMTP_PASS = "c2123a10c4bc7f"


def send_confirmation_email(order_data):
    sender_email = "test@laptopsales.com"
    receiver_email = order_data["email"]

    subject = f"Order Confirmation - {order_data['order_id']}"
    body = f"""
Hi {order_data['name']},

Thank you for your order!

Order ID: {order_data['order_id']}
Laptop Model: {order_data['laptopModel']}
Amount: ₹{order_data['amount']}
Status: Processing

We’ll notify you when your laptop is shipped.

Regards,  
Laptop Sales Team
"""

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(f"📧 Test email sent to {receiver_email} (Mailtrap)")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")


# Kafka Consumer
consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="order-consumer-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("✅ Kafka Consumer running. Press Ctrl+C to stop.\n")

try:
    for message in consumer:
        order_data = message.value

        print("📦 New Order Received from Kafka:")
        print(json.dumps(order_data, indent=4))

        # Update status in MongoDB
        result = orders_collection.update_one(
            {"order_id": order_data["order_id"]},
            {"$set": {"status": "Processing"}}
        )

        if result.modified_count > 0:
            print(f"✅ Order {order_data['order_id']} updated in MongoDB.\n")
            send_confirmation_email(order_data)
        else:
            print(f"⚠️ Order {order_data['order_id']} not found in DB.\n")

except KeyboardInterrupt:
    print("\n👋 Kafka Consumer stopped by user.")
finally:
    consumer.close()
    print("🔒 Kafka Consumer connection closed safely.")
