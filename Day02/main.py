import json
from fastapi import FastAPI, Path, HTTPException

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

# @app.get('/patient/{patient_id}')
# def view_patient(patient_id: str):
#     #load all the patients
#     data = load_data()

#     if patient_id in data:
#         return data[patient_id]
#     return {'error':'patient not found'}
#Now we will increase Readability of this function as specifying description about the ID through path function

# @app.get('/patient/{patient_id}')
# def view_patient(patient_id: str = Path(..., description='ID of patient in the DB', example='P001')):
#     #load all the patients
#     data = load_data()

#     if patient_id in data:
#         return data[patient_id]
#     return {'error':'patient not found'}
#now description is there but the problem is the HTTP status code for patient not found is still 200OK which should not be the case

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of patient in the DB', example='P001')):
    #load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not Found')

@app.get('/sort')
def sort_patients(sort_by: str)