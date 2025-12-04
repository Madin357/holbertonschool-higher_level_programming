#!/usr/bin/python3
"""
Flask application that reads product data from JSON, CSV, or SQLite database.
Uses ?source=json, ?source=csv, or ?source=sql
Optional ?id= filters a specific product.

Handles:
- Wrong source errors
- Product not found
- Invalid ID
- DB read errors
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)


# -------------------------
# --- File Reading Logic ---
# -------------------------

def read_json_file(filename):
    """Read and parse JSON file."""
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except Exception:
        return []


def read_csv_file(filename):
    """Read and parse CSV file."""
    products = []

    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row["id"] = int(row["id"])
                    row["price"] = float(row["price"])
                except ValueError:
                    pass
                products.append(row)
        return products
    except Exception:
        return []


def read_sql_data(db_file):
    """Read product data from SQLite database."""
    if not os.path.exists(db_file):
        return None  # Signals DB error

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3],
            })
        return products

    except Exception:
        return None  # DB error
        

# -------------------------
# ------ Flask Route -------
# -------------------------

@app.route('/products')
def products():
    """Display product data from JSON, CSV, or SQL."""
    source = request.args.get("source", "")
    product_id = request.args.get("id")

    error_message = None
    products_list = []

    # Determine source
    if source == "json":
        products_list = read_json_file("products.json")

    elif source == "csv":
        products_list = read_csv_file("products.csv")

    elif source == "sql":
        products_list = read_sql_data("products.db")
        if products_list is None:
            error_message = "Database error"
            return render_template("product_display.html", products=[], error=error_message)

    else:
        error_message = "Wrong source"
        return render_template("product_display.html", products=[], error=error_message)

    # Optional ID filtering
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
