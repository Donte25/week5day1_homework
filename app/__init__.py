from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    return "Hello"


@app.route("/html")
def index_html():
    favorite_things = ["Playing Video Games", "Singing", "Watching Anime", "Drawing", "Eating"]

    return render_template("index.html", message="My favorite things", red=True, html_favorite_things = favorite_things )


@app.route("/json")
def json():
    return {"message": "Hello from my API"}

app.run()