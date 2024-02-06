import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items


blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
         try:
            return items[item_id]
         except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item Deleted"}
        except KeyError:
            abort(404, message="Item not found")

    def put(self, item_id):
        item_data = request.get_json()
        if 'price' not in item_data or 'name' not in item_data:
            abort(400, message="Bad Request. Ensure 'price', 'name' are included in the JSON payload.")
        try:
            item = items[item_id]
            item |= item_data
            return item, 201
        except KeyError:
            abort(404, message="Item not found")


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}

    def post(self):
        item_data = request.get_json()
        if ("store_id" not in item_data
            or "name" not in item_data
            or "price" not in item_data):
            abort(400, message="Bad Request. Ensure 'price', 'store_id', 'name' are included in the JSON payload.")
        for item in items.values():
            if (item['store_id'] == item_data['store_id']
                and item['name'] == item_data['name']):
                abort(404, message="Item already exists in the store")
        if item_data["store_id"] not in stores:
            abort(404, message="Store not found")

        item_id = uuid.uuid4().hex
        item = {
            "id": item_id,
            **item_data
        }
        items[item_id] = item
        return item, 201



