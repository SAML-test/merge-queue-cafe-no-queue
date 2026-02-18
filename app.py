"""Merge Queue Café — a tiny Flask app for demoing GitHub merge queues."""

from flask import Flask, render_template

from menu import get_categories, get_menu

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", menu=get_menu(), categories=get_categories())


if __name__ == "__main__":
    app.run(debug=True)
