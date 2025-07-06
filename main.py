from fastapi import FastAPI;
from fastapi import HTTPException
from fastapi import Query
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

@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Key to sort by (weight, bmi, height)"),
    order: str = Query("asc", description="Sort order: asc or desc")):
    valid_keys=['weight', 'bmi', 'height']
    if sort_by not in valid_keys:
        raise HTTPException(
            status_code=400,
            detail="Invalid sort_by key. Must be one of: weight, bmi, height"
        )
    if order not in ['asc','desc']:
        raise HTTPException(
            status_code=400,
            detail="invalid order! order should be asc or desc"
        )
    data= load_data()
    reverse = order.lower() == "desc"
    sorted_data= sorted(data.values(), key= lambda x:x.get(sort_by,0), reverse=reverse)
    return sorted_data

