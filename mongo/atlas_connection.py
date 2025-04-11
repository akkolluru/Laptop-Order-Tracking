from pymongo import MongoClient

# Replace this with your MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://admin:<smart123>@laptop-sales.ye0na.mongodb.net/?retryWrites=true&w=majority&appName=Laptop-Sales"

def get_database():
    """Connect to MongoDB Atlas and return the database object."""
    client = MongoClient(MONGO_URI)
    db = client["LaptopOrders"]  # Database name
    return db

if __name__ == "__main__":
    db = get_database()
    print("Connected to MongoDB Atlas successfully!")

    # Create collections if they don’t exist
    db.create_collection("orders", check_exists=True)
    db.create_collection("customers", check_exists=True)
    db.create_collection("delivery", check_exists=True)
    
    print("Collections created!")
