# service/routers/itemvalues_api.py
from fastapi import APIRouter, HTTPException
from business.itemvalues_bl import ItemValuesBL

router = APIRouter(prefix="/itemvalues", tags=["itemvalues"])
bl = ItemValuesBL()


@router.get("/")
def get_all_values():
    return bl.get_all()


@router.get("/{value_id}")
def get_value(value_id: int):
    row = bl.get_one(value_id)
    if not row:
        raise HTTPException(status_code=404, detail="Item value not found")
    return row


# SUBSET example (required by Project 3):
@router.get("/by-item/{item_id}")
def get_values_for_item(item_id: int):
    return bl.get_subset_by_item(item_id)