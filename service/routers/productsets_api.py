# service/routers/productsets_api.py
from fastapi import APIRouter, HTTPException
from business.productsets_bl import ProductSetsBL

router = APIRouter(prefix="/productsets", tags=["productsets"])
bl = ProductSetsBL()


@router.get("/")
def get_all_sets():
    return bl.get_all()


@router.get("/{set_id}")
def get_set(set_id: int):
    row = bl.get_one(set_id)
    if not row:
        raise HTTPException(status_code=404, detail="Set not found")
    return row


# SUBSET example (required by Project 3):
@router.get("/by-year/{year}")
def get_sets_by_year(year: int):
    return bl.get_subset_by_year(year)