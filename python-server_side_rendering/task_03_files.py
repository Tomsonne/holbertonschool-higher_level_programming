from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception:
        return

def read_csv():
    products = []
    try:
        with open("products.csv", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        pass
    return products

@app.route("/products")
def display_products():
    source = request.args.get("source")
    id_str = request.args.get("id")

    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    else:
        return render_template("product_display.html", error="Wrong source")

    if id_str:
        try:
            id_int = int(id_str)
            filtered = [item for item in data if item["id"] == id_int]
            if not filtered:
                return render_template("product_display.html", error="Product not found")
            return render_template("product_display.html", products=filtered)
        except ValueError:
            return render_template("product_display.html", error="Invalid ID format")

    return render_template("product_display.html", products=data)

if __name__ == "__main__":
    app.run(debug=True)

