from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
    client.server_info()  # Test connection

    db = client[DATABASE_NAME]
    donations = db["donations"]

except Exception:
    donations = None


# ---------------- SAVE DONATION ----------------

def save_donation(name, amount, method):
    if donations is None:
        return

    donations.insert_one({
        "name": name,
        "amount": amount,
        "method": method
    })


# ---------------- GET DONATIONS ----------------

def get_donations():
    if donations is None:
        return []

    return list(donations.find())


# ---------------- DONATION COUNT ----------------

def donation_count():
    if donations is None:
        return 0

    return donations.count_documents({})