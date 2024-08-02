from pydantic import BaseModel, EmailStr


class MessageSchemas(BaseModel):
    message: str


class UserSchemas(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublicSchemas(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDBSchemas(UserSchemas):
    id: int
