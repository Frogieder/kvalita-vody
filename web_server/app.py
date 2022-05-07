from flask import Flask, render_template, request, redirect
import os

# print(os.getcwd())

app = Flask(__name__)


@app.route("/")
def homepaeg():
    return "Here it works"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

