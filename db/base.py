from functools import lru_cache
from typing import Dict, Optional
from uuid import UUID

from db.models.items import Item
from db.models.orders import Order
from db.models.users import User


class BaseStorage(object):
    def __init__(
        self,
        users: Dict[UUID, User] = None,
        items: Dict[UUID, Item] = None,
        orders: Dict[UUID, Order] = None,
    ) -> None:
        self.users = {} if users is None else users
        self.items = {} if items is None else items
        self.orders = {} if orders is None else orders

    def get_user_by_id(self, user_id: UUID) -> Optional[User]:
        return self.users.get(user_id, None)

    def get_user_by_email(self, email: str) -> Optional[User]:
        for user in self.users.values():
            if user.email == email:
                return user
        return None

    def create_user(self, **kwargs) -> User:
        user = User(**kwargs)
        self.users[user.id] = user
        return user

    def get_order_by_id(self, order_id: UUID) -> Optional[Order]:
        return self.orders.get(order_id, None)

    def get_order_by_user_id(self, user_id: UUID) -> Optional[Order]:
        for order in self.orders.values():
            if order.user_id == user_id:
                return order
        return None

    def create_order(self, **kwargs) -> Order:
        order = Order(**kwargs)
        self.orders[order.id] = order
        return order

    def add_order_item(
        self,
        order_id,
        item_id,
        quantity,
    ) -> Order:
        order = self.orders.get(order_id)
        quantity = order.order_items.get(item_id, 0) + quantity
        order.order_items[item_id] = quantity
        self.orders[order_id] = order
        return order

    def get_item_by_id(self, item_id) -> Item:
        return self.items.get(item_id, None)

    def create_item(self, **kwargs) -> Item:
        item = Item(**kwargs)
        self.items[item.id] = item
        return item


@lru_cache
def get_base_storage() -> BaseStorage:
    return BaseStorage()
