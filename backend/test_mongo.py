from pymongo import MongoClient

# Replace with your actual MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://arun:smart@laptop-sales.ye0na.mongodb.net/?retryWrites=true&w=majority&appName=laptop-sales"

try:
    print("🔄 Attempting to connect to MongoDB Atlas...")
    
    # Set timeout to 10 seconds to avoid hanging
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=10000)
    
    # Connect to the "LaptopOrders" database
    db = client["LaptopOrders"]
    
    # Try listing collections to check if connection is successful
    collections = db.list_collection_names()
    
    print("✅ Successfully connected to MongoDB Atlas!")
    print("📂 Collections in Database:", collections)

except Exception as e:
    print("❌ MongoDB Connection Failed:", e)
