#!/usr/bin/python3
"""
Flask application that reads product data from JSON or CSV files
and displays them using a single dynamic template.

Supports:
- ?source=json or ?source=csv
- ?id=x (optional)
"""

from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)


def read_json_file(filename):
    """Read and parse product JSON data."""
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except Exception:
        return []


def read_csv_file(filename):
    """Read and parse product CSV data."""
    products = []

    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert ID and price to proper types
                try:
                    row["id"] = int(row["id"])
                    row["price"] = float(row["price"])
                except ValueError:
                    pass
                products.append(row)
        return products
    except Exception:
        return []


@app.route('/products')
def products():
    """Display products based on source=json/csv and optional id."""
    source = request.args.get("source", "")
    product_id = request.args.get("id")

    error_message = None
    products_list = []

    # Determine the data source
    if source == "json":
        products_list = read_json_file("products.json")
    elif source == "csv":
        products_list = read_csv_file("products.csv")
    else:
        error_message = "Wrong source"
        return render_template("product_display.html",
                               products=[],
                               error=error_message)

    # Filter by ID if provided
    if product_id:
        try:
            pid = int(product_id)
            filtered = [p for p in products_list if int(p["id"]) == pid]
            if not filtered:
                error_message = "Product not found"
            products_list = filtered
        except ValueError:
            error_message = "Invalid product ID"
            products_list = []

    return render_template("product_display.html",
                           products=products_list,
                           error=error_message)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
