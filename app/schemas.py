from pydantic import BaseModel


class CarBase(BaseModel):
    model: str
    color: str
    horsepower: int


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int
    make: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    items: list[Car] = []

    class Config:
        orm_mode = True
