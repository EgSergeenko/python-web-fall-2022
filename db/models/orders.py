from typing import Dict
from uuid import UUID

from pydantic import Field

from db.models.base import IDMixin


class Order(IDMixin):
    user_id: UUID
    order_items: Dict[UUID, int] = Field(default_factory=dict)
