from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
# from werkzeug.exceptions import HTTPException
import datetime
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from fastapi.exceptions import HTTPException


app = FastAPI()

class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get('/', response_model=str)
def root():
    return "string"

@app.get('/dog', response_model=list)
def get_dogs(kind: str):
    l = []
    for k, v in dogs_db.items():
        if v.kind == kind:
            l.append(v)
    return l

@app.get('/dog/{pk}', response_model=Dog)
def get_dogs(pk: int):
    l = []
    for k, v in dogs_db.items():
        if v.pk == pk:
            return v
    raise HTTPException(status_code=409,
                            detail='No dog with such PK')


@app.post('/post')
def get_post():
    a = datetime.datetime.now()
    new_timestamp = Timestamp(id=post_db[-1].id+1, timestamp=a.hour)
    post_db.append(new_timestamp)
    return new_timestamp

@app.post('/dog')
def create_dog(name:str,pk:int,kind:str):
    for k, v in dogs_db.items():
        if v.pk == pk:
            raise HTTPException(status_code=409,
                            detail='Dog with such PK already exists')
    a = dogs_db.keys()
    new_dog = Dog(name=name, pk=pk, kind=kind)
    dogs_db[max(a)+1] = new_dog
    return new_dog

@app.patch('/dog/{pk}', response_model=Dog)
def update_dog(pk: int, name: str, kind: str):
    for k, v in dogs_db.items():
        if v.pk == pk:
            v.name = name
            v.kind = kind
            return v
    raise HTTPException(status_code=409,
                            detail='No dog with such PK')