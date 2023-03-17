from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def site_title():
    year_current = datetime.date.today().year
    return render_template("index.html", year = year_current)

@app.route("/<name>")
def name_guess(name):
    guess = requests.get(f"https://api.agify.io?name={name}")
    gender = requests.get(f"https://api.genderize.io?name={name}").json().get("gender")
    name = guess.json().get("name")
    age = guess.json().get("age")
    return render_template(
        "index.html",
        username = name,
        usergender = gender,
        userage = age)

# @app.route("/<name>")
# def name_guess(name):
#     guess = requests.get(f"https://api.agify.io?name={name}")
#     name = guess.text("name")
#     age = guess.text("age")
#     return render_template("index.html", username = name, userage = age)

if __name__ == "__main__":
    app.run(debug=True)