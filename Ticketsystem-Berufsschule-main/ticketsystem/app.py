from flask import Flask, render_template, request, redirect, session
from users import users

app = Flask(__name__)
app.secret_key = "secretkey"

tickets = [
    {"id":1,"name":"Login funktioniert nicht","creator":"Max","agent":"Support-Team","status":"Offen"},
    {"id":2,"name":"Laptop defekt","creator":"Arda","agent":"Support-Team","status":"In Bearbeitung"},
    {"id":3,"name":"Ticket schließen","creator":"Arda","agent":"Max","status":"Geschlossen"}
]


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username in users and users[username]["password"] == password:

        session["user"] = username
        session["role"] = users[username]["role"]

        return redirect("/meine_tickets")

    return redirect("/")


@app.route("/meine_tickets")
def meine_tickets():

    if "user" not in session:
        return redirect("/")

    user = session["user"]

    user_tickets = [t for t in tickets if t["creator"].lower() == user.lower()]

    return render_template(
        "meine_tickets.html",
        tickets=user_tickets,
        role=session["role"]
    )


@app.route("/ticketpool")
def ticketpool():

    if "user" not in session:
        return redirect("/")

    return render_template(
        "ticketpool.html",
        tickets=tickets,
        role=session["role"]
    )


@app.route("/auswertung")
def auswertung():

    if "user" not in session:
        return redirect("/")

    return render_template(
        "auswertung.html",
        role=session["role"]
    )


@app.route("/logout")
def logout():

    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)