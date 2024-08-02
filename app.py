from http import HTTPStatus

from fastapi import FastAPI

from schemas import MessageSchemas, UserDBSchemas, UserSchemas, UserPublicSchemas

app = FastAPI()


database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=MessageSchemas)
def index():
    return {"message": "Hello World"}


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublicSchemas)
def create_user(user: UserSchemas):
    user_with_id = UserDBSchemas(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id
