from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str = None
    
class ItemCreate(Item):
    pass