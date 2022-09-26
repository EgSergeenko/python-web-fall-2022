from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from api.v1.models.mappers import order_to_dto
from api.v1.models.orders import Order
from db.base import BaseStorage, get_base_storage

router = APIRouter(
    prefix='/api/v1/orders',
    tags=['orders'],
)


@router.get(
    '/{order_id}',
    response_model=Order,
)
def get_order(
    order_id: UUID,
    storage: BaseStorage = Depends(get_base_storage),
) -> Order:
    order_model = storage.get_order_by_id(order_id)
    if order_model is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Order not found',
        )
    return order_to_dto(order_model)


@router.post(
    '/{order_id}',
    response_model=Order,
)
def add_order_item(
    order_id: UUID,
    item_id: UUID,
    quantity: int,
    storage: BaseStorage = Depends(get_base_storage),
) -> Order:
    order_model = storage.get_order_by_id(
        order_id,
    )
    if order_model is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Order not found',
        )
    item_model = storage.get_item_by_id(
        item_id,
    )
    if item_model is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Item not found',
        )
    order_model = storage.add_order_item(
        order_id,
        item_id,
        quantity,
    )
    return order_to_dto(order_model)


@router.post(
    '',
)
def create_order(
    current_user_id: UUID,
    storage: BaseStorage = Depends(get_base_storage),
):
    user_model = storage.get_user_by_id(current_user_id)
    if user_model is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found',
        )
    order_model = storage.get_order_by_user_id(current_user_id)
    if order_model is not None:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='One order per user',
        )
    order_model = storage.create_order(
        user_id=current_user_id,
    )
    return order_to_dto(order_model)
