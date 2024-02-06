from flask import Flask
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

app = Flask(__name__)
app.config["PROPAGATE_EXCEPTION"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(StoreBlueprint)
api.register_blueprint(ItemBlueprint)


# http://127.0.0.1:5000/store - to be accessed this way


# @app.get("/store")
# def get_stores():
#     return {
#         "message": "Successful",
#         "stores": list(stores.values())
#     }
#
#
# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#     if 'name' not in store_data:
#         abort(400, message="Bad request. Ensure 'name' is included in the JSON payload")
#     for store in stores.values():
#         if store['name'] == store_data['name']:
#             abort(400, message=f"{store['name']} already exists")
#     store_id = uuid.uuid4().hex
#     new_store = {
#         "id": store_id,
#         **store_data
#     }
#     stores[store_id] = new_store
#     return new_store, 201
#
#
# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     try:
#         return stores[store_id], 200
#     except KeyError:
#         abort(404, message="Store not found")
#
#
# @app.delete("/store/<string:store_id>")
# def delete_store(store_id):
#     try:
#         del stores[store_id]
#         return {"message": "Store Deleted"}
#     except KeyError:
#         abort(404, message="Store not found")
#
#
# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}
#
#
# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     if ("store_id" not in item_data
#         or "name" not in item_data
#         or "price" not in item_data):
#         abort(400, message="Bad Request. Ensure 'price', 'store_id', 'name' are included in the JSON payload.")
#     for item in items.values():
#         if (item['store_id'] == item_data['store_id']
#             and item['name'] == item_data['name']):
#             abort(404, message="Item already exists in the store")
#     if item_data["store_id"] not in stores:
#         abort(404, message="Store not found")
#
#     item_id = uuid.uuid4().hex
#     item = {
#         "id": item_id,
#         **item_data
#     }
#     items[item_id] = item
#     return item, 201
#
#
# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404, message="Item not found")
#
#
# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message": "Item Deleted"}
#     except KeyError:
#         abort(404, message="Item not found")
#
#
# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data = request.get_json()
#     if 'price' not in item_data or 'name' not in item_data:
#         abort(400, message="Bad Request. Ensure 'price', 'name' are included in the JSON payload.")
#     try:
#         item = items[item_id]
#         item |= item_data
#         return item, 201
#     except KeyError:
#         abort(404, message="Item not found")
