from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from models import UserModels
from schemas import (
    MessageSchemas,
    UserList,
    UserPublicSchemas,
    UserSchemas,
)
from security import (
    get_current_user,
    get_password_hash,
)

Session = Annotated[Session, Depends(get_session)]

CurrentUser = Annotated[UserModels, Depends(get_current_user)]

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/users/", status_code=HTTPStatus.CREATED, response_model=UserPublicSchemas
)
def create_user(user: UserSchemas, session: Session = Session):
    db_user = session.scalar(
        select(UserModels).where(
            (UserModels.username == user.username) | (UserModels.email == user.email)
        )
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Username already exists",
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Email already exists",
            )
    hashed_password = get_password_hash(user.password)

    db_user = UserModels(
        username=user.username, password=hashed_password, email=user.email
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.get("/users/", response_model=UserList)
def read_users(skip: int = 0, limit: int = 100, session: Session = Session):
    users = session.scalars(select(UserModels).offset(skip).limit(limit)).all()
    return {"users": users}


@router.put("/users/{user_id}", response_model=UserPublicSchemas)
def update_user(
    user_id: int, user: UserSchemas, session: Session, current_user: CurrentUser
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail="Not enough permissions"
        )

    current_user.username = user.username
    current_user.password = get_password_hash(user.password)
    current_user.email = user.email
    session.add(current_user)
    session.commit()
    session.refresh(current_user)

    return current_user


@router.delete("/users/{user_id}", response_model=MessageSchemas)
def delete_user(
    user_id: int,
    session: Session,
    current_user: CurrentUser,
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail="Not enough permissions"
        )

    session.delete(current_user)
    session.commit()

    return {"message": "User deleted"}
