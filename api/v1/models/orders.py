from typing import Dict
from uuid import UUID

from pydantic import BaseModel, Field


class Order(BaseModel):
    order_items: Dict[UUID, int] = Field(default_factory=dict)
