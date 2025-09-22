#from flask import Flask

#app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello World"

#if __name__ == "__main__":
#    app.run(debug=True)

from flask import Flask, jsonify, request

app = Flask(__name__)

# Step 4: seed items
items = [
    {
        "id": 1,
        "name": "Laptop",
        "manufacturer": "Dell",
        "sku": "LAP123",
        "price": 120000  # pennies = £1200.00
    },
    {
        "id": 2,
        "name": "Mouse",
        "manufacturer": "Logitech",
        "sku": "MOU456",
        "price": 2000  # pennies = £20.00
    }
]


# Step 6 GET all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

# Step 7 GET item by ID
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Step 10 CREATE new item
@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()  # read JSON body
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    new_id = max(item["id"] for item in items) + 1 if items else 1
    new_item = {
        "id": new_id,
        "name": data.get("name"),
        "manufacturer": data.get("manufacturer"),
        "sku": data.get("sku"),
        "price": data.get("price")
    }
    items.append(new_item)
    return jsonify(new_item), 201

# Step 11 Modify an existing item
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    for item in items:
        if item["id"] == item_id:
            # update allowed fields, but don't allow changing the ID
            item["name"] = data.get("name", item["name"])
            item["manufacturer"] = data.get("manufacturer", item["manufacturer"])
            item["sku"] = data.get("sku", item["sku"])
            item["price"] = data.get("price", item["price"])
            return jsonify(item)

    return jsonify({"error": "Item not found"}), 404

# Step 12 DELETE item by ID
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return jsonify({"message": "Item deleted successfully"})
    return jsonify({"error": "Item not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

