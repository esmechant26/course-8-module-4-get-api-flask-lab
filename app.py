from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]


# Homepage
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Product API!"})


# Get all products, optionally filtered by category
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")

    if category:
        filtered_products = [
            product for product in products
            if product["category"] == category
        ]
        return jsonify(filtered_products)

    return jsonify(products)


# Get one product by ID
@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = next(
        (product for product in products if product["id"] == id),
        None
    )

    if product:
        return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)