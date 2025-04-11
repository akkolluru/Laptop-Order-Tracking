from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

# Correct MongoDB connection string
MONGO_URI = f"mongodb+srv://arun:smart@laptop-sales.ye0na.mongodb.net/?retryWrites=true&w=majority&appName=laptop-sales"

try:
    # Set a timeout of 10 seconds
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=10000)
    db = client["LaptopOrders"]
    
    # Test connection
    print("✅ Connected to MongoDB Atlas successfully!")

    # Test inserting a document
    sample_order = {
        "order_id": "ORD1234",
        "customer_id": "CUST5678",
        "laptop_model": "Model A",
        "amount": 1000,
        "order_date": "2025-02-17",
        "status": "Pending"
    }

    db.orders.insert_one(sample_order)  # This should complete instantly
    print("✅ Successfully inserted a sample order!")

    # List collections
    collections = db.list_collection_names()
    print("Collections:", collections)

except ServerSelectionTimeoutError as e:
    print("❌ Connection Timeout: Unable to reach MongoDB Atlas")
    print("Error:", e)

except Exception as e:
    print("❌ Connection Error:", e)
