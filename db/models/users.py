from db.models.base import IDMixin


class User(IDMixin):
    name: str
    email: str
