from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from business.items_bl import ItemsBL

router = APIRouter(prefix="/items", tags=["items"])
bl = ItemsBL()

class ItemCreate(BaseModel):
    user_id: int
    set_id: int
    item_name: str
    sealed: bool = True

@router.get("/")
def get_all():
    return bl.get_all_items()

@router.get("/{item_id}")
def get_one(item_id: int):
    item = bl.get_item_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/")
def create(body: ItemCreate):
    try:
        new_id = bl.create_item(body.user_id, body.set_id, body.item_name, body.sealed)
        return {"item_id": new_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{item_id}")
def update(item_id: int, body: ItemCreate):
    rows = bl.update_item(item_id, body.user_id, body.set_id, body.item_name, body.sealed)
    if rows == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"updated": True}

@router.delete("/{item_id}")
def delete(item_id: int):
    rows = bl.delete_item(item_id)
    if rows == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"deleted": True}