import json
from fastapi import FastAPI

app = FastAPI()

#function to load data from json file
def load_data():
    with open ('patients.json', 'r') as f:
        data = json.load(f)

    return data

@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')
def about():
    return {'message':'A fully functional API to manage your patient records'}


#Creating Endpoint to retireve data
@app.get('/view')
def view():
    data = load_data()

    return data

