from flask import Flask, render_template, request, redirect, url_for, flash

from database.mysql_db import (
    save_volunteer,
    get_volunteers,
    save_contact,
    get_contacts
)

from database.mongo_db import (
    save_donation,
    get_donations,
    donation_count
)

app = Flask(__name__)
app.secret_key = "aashraya_secret_key"


# ---------------- HOME ----------------

@app.route("/")
def home():

    try:
        total = donation_count()
    except Exception:
        total = 0

    return render_template(
        "index.html",
        total=total
    )


# ---------------- ABOUT ----------------

@app.route("/about")
def about():

    return render_template("about.html")


# ---------------- SERVICES ----------------

@app.route("/services")
def services():

    return render_template("services.html")


# ---------------- GALLERY ----------------

@app.route("/gallery")
def gallery():

    return render_template("gallery.html")


# ---------------- DONATE ----------------

@app.route("/donate")
def donate():

    return render_template("donate.html")


# ---------------- CONTACT ----------------

@app.route("/contact")
def contact():

    return render_template("contact.html")


# ---------------- VOLUNTEER ----------------

@app.route("/volunteer")
def volunteer():

    return render_template("volunteer.html")


# ------------------------------------------------
# SAVE VOLUNTEER
# ------------------------------------------------

@app.route("/save_volunteer", methods=["POST"])
def volunteer_save():

    name = request.form["name"]

    phone = request.form["phone"]

    email = request.form["email"]

    address = request.form["address"]

    save_volunteer(
        name,
        phone,
        email,
        address
    )

    flash("Volunteer Registered Successfully")

    return redirect("/volunteer")


# ------------------------------------------------
# SAVE CONTACT
# ------------------------------------------------

@app.route("/save_contact", methods=["POST"])
def contact_save():

    name = request.form["name"]

    email = request.form["email"]

    message = request.form["message"]

    save_contact(
        name,
        email,
        message
    )

    flash("Message Sent Successfully")

    return redirect("/contact")


# ------------------------------------------------
# SAVE DONATION
# ------------------------------------------------

@app.route("/save_donation", methods=["POST"])
def donation_save():

    name = request.form["name"]

    amount = request.form["amount"]

    method = request.form["method"]

    save_donation(
        name,
        amount,
        method
    )

    flash("Donation Submitted Successfully")

    return redirect("/donations")


# ------------------------------------------------
# VIEW DONATIONS
# ------------------------------------------------

@app.route("/donations")
def donations():

    data = get_donations()

    return render_template(
        "donation_table.html",
        donations=data
    )


# ------------------------------------------------
# VIEW VOLUNTEERS
# ------------------------------------------------

@app.route("/volunteers")
def volunteers():

    data = get_volunteers()

    return render_template(
        "volunteers.html",
        volunteers=data
    )


# ------------------------------------------------
# VIEW CONTACTS
# ------------------------------------------------

@app.route("/contacts")
def contacts():

    data = get_contacts()

    return render_template(
        "contacts.html",
        contacts=data
    )


# ------------------------------------------------
# ADMIN PAGE
# ------------------------------------------------

@app.route("/admin")
def admin():

    volunteers = get_volunteers()

    contacts = get_contacts()

    donations = get_donations()

    return render_template(

        "admin.html",

        volunteers=volunteers,

        contacts=contacts,

        donations=donations

    )

# ------------------------------------------------
# GOOGLE SEARCH CONSOLE VERIFICATION
# ------------------------------------------------

@app.route("/googlee5ec18d9718ee57a.html")
def google_verification():
    return send_from_directory(".", "googlee5ec18d9718ee57a.html")
# ------------------------------------------------
# RUN APP
# ------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )