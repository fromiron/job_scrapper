from flask import Flask, render_template, request
from stackoverflow import stackoverflow_finder
from weworkremotely import weworkremotely_finder
from remoteok import remoteok_finder

app = Flask("job scrapper")

stack_db = {}
remote_db = {}
wework_db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search", methods=["POST"])
def post():
    word = request.form["word"]
    if word in stack_db.keys():
        pass
    else:
        stack_db[word] = stackoverflow_finder(word)
        wework_db[word] = weworkremotely_finder(word)
        remote_db[word] = remoteok_finder(word)
    return render_template(
        "search.html",
        stack=stack_db[f"{word}"],
        wework=wework_db[f"{word}"],
        remote=remote_db[f"{word}"],
    )


app.run()
