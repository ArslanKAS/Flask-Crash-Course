from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    year_current = datetime.date.today().year
    return render_template("index.html", year = year_current)
    # render template is used to fetch the html pages and send Python code to them

@app.route("/guess/<name>")
def name_guess(name):
    # APIs usually require .json() at the end so we can deal with them as Dictionaries
    guess = requests.get(f"https://api.agify.io?name={name}")
    gender = requests.get(f"https://api.genderize.io?name={name}").json().get("gender")
    name = guess.json().get("name")
    age = guess.json().get("age")
    return render_template(
        "guess.html",
        username = name,
        usergender = gender,
        userage = age)

@app.route("/blogs/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c25db3e99a1dc2a58b18"
    blogs = requests.get(blog_url).json()
    return render_template("blog.html", blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True)