import os
from json import dump as json_dump
from json import load as json_load
from json.decoder import JSONDecodeError

from flask import Flask, render_template

JSON_PATH = "/usr/src/app/data/iframe_links.json"
# JSON_PATH = "iframe_links.json"

DEFAULT_DICTIONARY = dict(
    orp="https://streamable.com/e/shil2",
    ph="https://streamable.com/e/shil2",
    clarity="https://streamable.com/e/shil2",
    temperature="https://streamable.com/e/shil2",
    oxygen="https://streamable.com/e/shil2"
)

## Load the links for the iframe, create the required file if necessary 
if not os.path.isfile(JSON_PATH):
    with open(JSON_PATH, "w") as file:
        json_dump(DEFAULT_DICTIONARY, file)
try:
    with open(JSON_PATH, "r") as file:
        iframe_links = json_load(file)
except JSONDecodeError:
    print("Problem decoding json file")
    iframe_links = DEFAULT_DICTIONARY

iframes = [{"name":name, "url":iframe_links[name]} for name in iframe_links]

# Create the web server
app = Flask(__name__)


@app.route("/")
def homepaeg(): # Not a typo
    return render_template("index.html", iframes=iframes)


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5001)
    print("WSGI server running at 0.0.0.0:5001")
    from waitress import serve
    serve(app, host="0.0.0.0", port=5001)
