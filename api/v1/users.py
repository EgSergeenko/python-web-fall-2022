from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from api.v1.models.mappers import user_to_dto
from api.v1.models.users import User
from db.base import BaseStorage, get_base_storage

router = APIRouter(
    prefix='/api/v1/users',
    tags=['users'],
)


@router.get(
    '/{user_id}',
    response_model=User,
)
def get_user(
    user_id: UUID,
    storage: BaseStorage = Depends(get_base_storage),
) -> User:
    user_model = storage.get_user_by_id(
        user_id,
    )
    if user_model is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found',
        )
    return user_to_dto(user_model)


@router.post(
    '',
)
def create_user(
    user: User,
    storage: BaseStorage = Depends(get_base_storage),
) -> User:
    if storage.get_user_by_email(user.email) is None:
        user_model = storage.create_user(
            **user.dict(),
        )
        return user_to_dto(user_model)
    raise HTTPException(
        status_code=HTTPStatus.CONFLICT,
        detail='User with this email already exists',
    )
