from fastapi import FastAPI, HTTPException # type: ignore
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text : str = None
    isDone : bool = False

items = []

# CREATE
@app.post("/items")
def create_item(item : Item):
    items.append(item)
    return items


# READ
@app.get("/")
def root():
    return {"hello" : "world"}

@app.get("/items", response_model = list[Item])
def get_items(limit : int = 10):
    return items[0:limit]

@app.get("/items/{item_id}", response_model = Item)
def get_item(item_id : int) -> Item:
    if item_id < len(items):
        item = items[item_id]
        return item
    else:
        raise HTTPException(status_code = 404, detail = f"Item {item_id} not found")


# UPDATE
@app.put("/items/togglecompletion", response_model = Item)
def toggle_completion(item_id : int) -> Item:
    if item_id > len(items):
        raise HTTPException(status_code = 404, detail = f"Item {item_id} not found")
    
    item = items[item_id]
    updatedItem = item.copy(update={"isDone": not item.isDone})
    items[item_id] = updatedItem
    
    return updatedItem


# DELETE
@app.delete("/items")
def remove_all_items():
    items.clear()
    return items