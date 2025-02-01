from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = randint(1, 10)
    year = datetime.now().year
    return render_template("index.html", num=random_number, year=year)

@app.route("/guess/<name>")
def guess(name):
    params = {
        "name": name
    }

    age_response = requests.get(url="https://api.agify.io", params=params)
    age_response.raise_for_status()
    age = age_response.json()["age"]

    gender_response = requests.get(url="https://api.genderize.io", params=params)
    gender_response.raise_for_status()
    gender = gender_response.json()['gender']

    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/36add2dec3c27aadeeef"
    blog_response = requests.get(url=blog_url)
    blog_response.raise_for_status()
    blog_posts = blog_response.json()
    return render_template("blog.html", posts=blog_posts, num=num)

if __name__ == "__main__":
    app.run(debug=True)