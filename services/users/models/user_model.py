"""
    По сути валидация данных ответа
"""

from pydantic import BaseModel, field_validator


class UserModel(BaseModel):
    email: str
    name: str
    nickname: str
    uuid: str

    # декоратор pydantic для валидации полей
    @field_validator('email', 'name', 'nickname', 'uuid')
    # кастомный валидатор для полей
    def fields_are_not_empty(cls, value):  # cls - данный метод относится только к этому классу
        if value == "" or value is None:  # не None и не пустое
            raise ValueError("Field is empty")  # raise поднятие кастомного исключения
        return value
