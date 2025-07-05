from fastapi import FastAPI;
from fastapi import HTTPException
import json
app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)

    return data

@app.get("/")
def hello():
    return {'message': 'Patient management system API'}

@app.get("/about")
def about():
    return {'message': 'A fully functional API to manage patient records.'}

@app.get("/view")
def view():
    data= load_data()
    return data

@app.get("/patient/{patient_id}")
def get_patient(patient_id: str):
    #load the patient data
    data= load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(
        status_code=404,
        detail=f"Patient {patient_id} not found."
    )
