from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from business.productsets_bl import ProductSetsBL

router = APIRouter(prefix="/productsets", tags=["productsets"])
bl = ProductSetsBL()

class ProductSetCreate(BaseModel):
    set_name: str
    release_year: int

@router.get("/")
def get_all():
    return bl.get_all_sets()

@router.get("/{set_id}")
def get_one(set_id: int):
    try:
        row = bl.get_set_by_id(set_id)
        if row is None:
            raise HTTPException(status_code=404, detail="Product set not found")
        return row
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/by-year/{year}")
def get_by_year(year: int):
    try:
        return bl.get_sets_by_year(year)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/")
def create(body: ProductSetCreate):
    try:
        new_id = bl.create_set(body.set_name, body.release_year)
        return {"set_id": new_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))