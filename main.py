from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserDetails(BaseModel):
    name:str
    age:int
    desig:str


#data in normal way
@app.post('/userdetails')
def getUserDetails(name:str,age:int):
    return {
        'message':'User Details',
        'details':{'name':name,'age':age}
    }

#taken as dictionary
@app.post('/userdetailsnew')
def getUserDetailsNew(user:dict):
    return {
        'message':'User Details',
        'details':user
    }

#using Pydantic - for validated data and structure defined
@app.post('/userdetailspydantic')
def getUserDetailsPydantic(user:UserDetails):
    return {
        'message':'User Details',
        'details':user
    }


