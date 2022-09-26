from api.v1.models.items import Item as ItemDto
from api.v1.models.orders import Order as OrderDto
from api.v1.models.users import User as UserDto
from db.models.items import Item as ItemModel
from db.models.orders import Order as OrderModel
from db.models.users import User as UserModel


def user_to_dto(user_model: UserModel) -> UserDto:
    return UserDto(
        name=user_model.name,
        email=user_model.email,
    )


def order_to_dto(order_model: OrderModel) -> OrderDto:
    return OrderDto(
        order_items=order_model.order_items,
    )


def item_to_dto(item_model: ItemModel) -> ItemDto:
    return ItemDto(
        name=item_model.name,
        price=item_model.price,
        description=item_model.description,
    )
