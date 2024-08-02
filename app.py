from fastapi import FastAPI
from http import HTTPStatus
from schemas import UserSchemas, UserPublicSchemas, UserDBSchemas, MessageSchemas

app = FastAPI()


database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=MessageSchemas)
def index():
    return {"message": "Hello World"}


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublicSchemas)
def create_user(user: UserSchemas):
    user_with_id = UserDBSchemas(id=len(database) + 1, **user.mmodel_dump())
    database.append(user_with_id)
    return database
