from fastapi import FastAPI;
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

print(load_data()['P001']['name'])
