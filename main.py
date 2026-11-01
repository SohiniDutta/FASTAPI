from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return "Hello"

@app.get('/about/')
def about():
    return "This is about page"

@app.get('/users/')
def userslist():
    return {'users':['Sita','Geeta','Lolita']}

#Path Parameters with type define and validation check
@app.get('/user/{user_id}')
def getUser(user_id:int):
    return f'this is the value : {user_id}'

#Query Parameters
@app.get('/product/')
def getProduct(name:str = 'Anonymous',page:int=1,price:float=None):
    return {
          'name':name,
          'page':page,
          'price':price
    }
#Path parameters are part of the URL path. They usually identify a specific resource or record.
#Query parameters are added after ? in the URL.They are generally used for filtering, searching, sorting and pagination
# Query parameters are not declared inside the route URL..
# Path parameter {user_id} is defined inside the route.
