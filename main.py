from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city:str
    pin:int

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post('/createUser')
def createUser(user:User):
    return {
        'message':'User Data',
        'details':user
    }


