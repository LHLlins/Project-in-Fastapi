from typing import List

from pydantic import BaseModel, ConfigDict, EmailStr

from models import TodoState


class MessageSchemas(BaseModel):
    message: str


class UserSchemas(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDBSchemas(UserSchemas):
    id: int


class UserPublicSchemas(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: List[UserPublicSchemas]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class TodoSchemas(BaseModel):
    title: str
    description: str
    state: TodoState


class TodoPublicSchemas(TodoSchemas):
    id: int


class TodoList(BaseModel):
    todos: list[TodoPublicSchemas]


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    state: TodoState | None = None
