from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, models, schemas

router = APIRouter(
    tags=["items"],
    prefix="/api/items",
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)


@router.post("/")
def post_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@router.get("/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    return crud.get_item(db=db, item_id=item_id)


@router.put("/{item_id}")
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.update_item(db=db, item_id=item_id, item=item)

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_item(db=db, item_id=item_id)   
    