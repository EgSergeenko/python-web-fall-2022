from pydantic import BaseModel, confloat


class Item(BaseModel):
    name: str
    price: confloat(gt=0)
    description: str
