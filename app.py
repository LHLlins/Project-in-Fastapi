from http import HTTPStatus

from fastapi import FastAPI

from routers import auth, todos, users
from schemas import MessageSchemas

app = FastAPI()


app.include_router(users.router)

app.include_router(auth.router)

app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=MessageSchemas)
def index():
    return {'message': 'Hello World'}
