from pymongo import MongoClient

# MongoDB Connection URI
MONGO_URI = "mongodb+srv://arun:smart@laptop-sales.ye0na.mongodb.net/?retryWrites=true&w=majority&appName=laptop-sales"

# Function to get database connection
def get_database():
    client = MongoClient(MONGO_URI)
    db = client["LaptopOrders"]  # Database Name
    return db

# Test connection when running this file directly
if __name__ == "__main__":
    db = get_database()
    print("✅ Connected to MongoDB Atlas successfully!")
    print("📂 Collections:", db.list_collection_names())
