#!/usr/bin/python3
"""
Flask application that displays items loaded from a JSON file
using Jinja loops and conditionals.
"""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)


@app.route('/items')
def items():
    """Route to display items from a JSON file."""

    items_list = []

    # Read items.json
    if os.path.exists("items.json"):
        try:
            with open("items.json", "r") as file:
                data = json.load(file)
                items_list = data.get("items", [])
        except Exception:
            items_list = []

    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
