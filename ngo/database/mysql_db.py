import mysql.connector
from config import MYSQL_CONFIG


# ---------------- CONNECT ----------------

def get_connection():

    return mysql.connector.connect(**MYSQL_CONFIG)


# ---------------- SAVE VOLUNTEER ----------------

def save_volunteer(name, phone, email, address):

    db = get_connection()

    cursor = db.cursor()

    sql = """
    INSERT INTO volunteers
    (name,phone,email,address)
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(sql, (name, phone, email, address))

    db.commit()

    cursor.close()

    db.close()


# ---------------- GET VOLUNTEERS ----------------

def get_volunteers():

    db = get_connection()

    cursor = db.cursor()

    cursor.execute("SELECT * FROM volunteers")

    data = cursor.fetchall()

    cursor.close()

    db.close()

    return data


# ---------------- SAVE CONTACT ----------------

def save_contact(name, email, message):

    db = get_connection()

    cursor = db.cursor()

    sql = """
    INSERT INTO contact
    (name,email,message)
    VALUES(%s,%s,%s)
    """

    cursor.execute((sql), (name, email, message))

    db.commit()

    cursor.close()

    db.close()


# ---------------- GET CONTACT ----------------

def get_contacts():

    db = get_connection()

    cursor = db.cursor()

    cursor.execute("SELECT * FROM contact")

    data = cursor.fetchall()

    cursor.close()

    db.close()

    return data