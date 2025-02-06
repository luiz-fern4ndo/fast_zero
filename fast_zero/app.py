from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserPublic, UserSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def ready_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', response_model=UserPublic)
def create_users(user: UserSchema):
    return user
