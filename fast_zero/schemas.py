from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    usename: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    usename: str
    email: EmailStr
