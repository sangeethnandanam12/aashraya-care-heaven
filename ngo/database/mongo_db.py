from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME


client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

donations = db["donations"]


# ---------------- SAVE DONATION ----------------

def save_donation(name, amount, method):

    donations.insert_one({

        "name": name,

        "amount": amount,

        "method": method

    })


# ---------------- GET DONATIONS ----------------

def get_donations():

    return list(donations.find())


# ---------------- DONATION COUNT ----------------

def donation_count():

    return donations.count_documents({})