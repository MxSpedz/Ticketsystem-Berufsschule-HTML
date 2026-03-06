from flask import Flask, render_template, request
from users import users

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    for user in users:
        if user["username"] == username and user["password"] == password:
            return "Login erfolgreich!"

    return "Falscher Benutzername oder Passwort"

if __name__ == "__main__":
    app.run(debug=True)
