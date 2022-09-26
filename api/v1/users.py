from typing import List

from fastapi import APIRouter

from api.v1.models.users import User

router = APIRouter(
    prefix='/api/v1/users',
    tags=['users'],
)


@router.get(
    '/search',
    response_model=List[User],
)
def search_users(name: str) -> List[User]:
    return [
        User(
            name='Egor Sergeenko',
            email='es.egor.sergeenko@gmail.com',
        ),
        User(
            name='Egor Sergeenko',
            email='egor.sergeenko.es@gmail.com',
        ),
    ]


@router.get(
    '/{user_id}',
    response_model=User,
)
def get_user(user_id: int) -> User:
    return User(
        name='Egor Sergeenko',
        email='es.egor.sergeenko@gmail.com',
    )


@router.post(
    '',
    response_model=User,
)
def create_user(user: User) -> User:
    return user
