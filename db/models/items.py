from pydantic import confloat

from db.models.base import IDMixin


class Item(IDMixin):
    name: str
    price: confloat(gt=0)
    description: str
