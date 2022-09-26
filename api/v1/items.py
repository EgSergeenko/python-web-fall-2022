from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from api.v1.models.items import Item
from api.v1.models.mappers import item_to_dto
from db.base import BaseStorage, get_base_storage

router = APIRouter(
    prefix='/api/v1/items',
    tags=['items'],
)


@router.get(
    '/item_id}',
    response_model=Item,
)
def get_item(
    item_id: UUID,
    storage: BaseStorage = Depends(get_base_storage),
) -> Item:
    item_model = storage.get_item_by_id(
        item_id,
    )
    if item_model is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Item not found',
        )
    return item_to_dto(item_model)


@router.post(
    '',
    response_model=Item,
)
def create_item(
    item: Item,
    storage: BaseStorage = Depends(get_base_storage),
) -> Item:
    item_model = storage.create_item(
        **item.dict(),
    )
    return item_to_dto(item_model)
