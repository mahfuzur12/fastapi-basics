# FastAPI CRUD API

A basic REST API built with [FastAPI](https://fastapi.tiangolo.com/). Implemented basic CRUD (Create, Read, Update, Delete) operations using FastAPI and Pydantic.

## Project Overview
The API allows users to manage a list of items, each represented by a simple model. The following operations are supported:
- **Create**: Add new items to the list.
- **Read**: Retrieve one or more items.
- **Update**: Toggle the completion status of an item.
- **Delete**: Clear all items from the list.

## Data Model
The `Item` model is defined using Pydantic:
```python
class Item(BaseModel):
    text: str  # Description or content of the item
    isDone: bool = False  # Completion status, defaults to False
```
- `text`: A required string field representing the description of the item.
- `isDone`: A boolean field indicating whether the item is completed (default: `False`).

## Endpoints
### 1. Create Item
**Endpoint**: `POST /items`

**Description**: Adds a new item to the list.

**Request Body**:
```json
{
  "text": "Sample task",
  "isDone": false
}
```

**Response**:
Returns the updated list of items.

---

### 2. Retrieve All Items
**Endpoint**: `GET /items`

**Description**: Retrieves a list of items, with an optional limit on the number of items returned.

**Query Parameter**:
- `limit`: (Optional) Maximum number of items to retrieve. Default: `10`.

**Response**:
```json
[
  {
    "text": "Sample task",
    "isDone": false
  }
]
```

---

### 3. Retrieve a Single Item
**Endpoint**: `GET /items/{item_id}`

**Description**: Retrieves a single item by its ID.

**Path Parameter**:
- `item_id`: Index of the item in the list (0-based).

**Response**:
```json
{
  "text": "Sample task",
  "isDone": false
}
```

**Error Response**:
```json
{
  "detail": "Item {item_id} not found"
}
```

---

### 4. Toggle Completion Status
**Endpoint**: `PUT /items/togglecompletion`

**Description**: Toggles the `isDone` status of an item.

**Query Parameter**:
- `item_id`: Index of the item in the list (0-based).

**Response**:
```json
{
  "text": "Sample task",
  "isDone": true
}
```

**Error Response**:
```json
{
  "detail": "Item {item_id} not found"
}
```

---

### 5. Remove All Items
**Endpoint**: `DELETE /items`

**Description**: Clears all items from the list.

**Response**:
```json
{
  "message": "All items have been removed"
}
```

## Running the API
1. Install dependencies:
   ```bash
   pip install fastapi pydantic uvicorn
   ```
   or
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
3. Access the interactive documentation (or use Postman) at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

