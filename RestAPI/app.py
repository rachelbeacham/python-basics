# Create a flask app. The name app.py & the variable app is important
from flask import Flask, request
from db import items, stores
from flask_smorest import abort
import uuid
app = Flask(__name__)

# Run the app by activating virtual environment
  # cd dev/venvs/pythonUdemyEnv/bin  then run command `source activate`
# Then once inside the RestAPI folder, run the app using command `flask run`
  # Once app is running you'll se `Running on http://127.0.0.1:5000`
  # Press Ctrl + C to stop the app - will need to stop and restart after any changes ###for now
# Deactivate virtual env with command `deactivate` from anywhere

@app.get('/store') # Creates a new endpoint - http://127.0.0.1:5000/store  -- can run in browser
def get_stores(): # endpoint is associated with get_stroes function
  return {"stores": list(stores.values())}

@app.post('/store') # send post requests with a api client like insomnia
def create_store():
  store_data = request.get_json()
  if "name" not in store_data:
    abort(400, message="Bad Request. Ensure 'name' is included in the JSON payload.")
  for store in stores.values():
    if store_data['name'] == store['name']:
      abort(400, message=f"Store, {store_data['name']}, already exists")
  store_id = uuid.uuid4().hex
  store = {**store_data, "id": store_id}
  stores[store_id] = store
  return store, 201

@app.post('/item') ## Specific store name is in the url - we can access it with this notation, then use it as a parameter to create_item
def create_item():
  item_data = request.get_json()
  # Validate all the data required is received
  if (
    "price" not in item_data
    or "store_id" not in item_data
    or "name" not in item_data
  ):
    abort(400,
    message="Bad Request. Ensure 'price', 'store_id' and 'name' are included in the JSON payload."
    )
  # Validate we are not duplicating items in stores
  for item in items.values():
    if (
      item_data['name'] == item['name']
      and item_data['store_id'] == item['store_id']
    ):
      abort(400, message="Item already exists.")
  # Validate that the store exists
  if item_data['store_id'] not in stores:
    abort(404, message="Store not found")

  item_id = uuid.uuid4().hex
  item = {**item_data, "id": item_id}
  items[item_id] = item
  return item, 201

@app.get('/item')
def get_all_items():
  return {"items": list(items.values())}

@app.get('/store/<string:store_id>')
def get_store(store_id):
  try:
    return stores[store_id]
  except KeyError:
    abort(404, message="Store not found")

@app.get('/item/<string:item_id>')
def get_item(item_id):
  try:
    return items[item_id]
  except KeyError:
    return {"message": "Item not found"}, 404

@app.delete('/item/<string:item_id>')
def delete_item(item_id):
  try:
    del items[item_id]
    return{"message": "Item Deleted"}
  except KeyError:
    return {"message": "Item not found"}, 404

@app.put('/item/<string:item_id>')
def update_item(item_id):
  item_data = request.get_json()
  if "store_id" in item_data:
    abort(400, message="Cannot update the 'store_id', only 'price' or 'name'.")

## abort does the same thing as the manual return 404 with json message
