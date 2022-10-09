from fastapi import APIRouter, Request
from models import CpfStr, Limit, PatientCreate, PatientUpdate

def canUseCpf(request: Request, cpf: int):
    if request.app.database.patients.find_one({"cpf": cpf}):
        return False
    return True

patient = APIRouter(prefix="/patient", tags=["patient"])

@patient.post("/")
def create_patient(request: Request, patient: PatientCreate):
    patient_dict = dict(patient)
    if canUseCpf(request, patient_dict["cpf"]):
        new_patient = request.app.database.patients.insert_one(patient_dict)
        return request.app.database.patients.find_one({"_id": new_patient.inserted_id}, {"_id": False})
    return "cpf is already registered."

@patient.get("/")
def read_patients(request: Request, skip: int = 0, limit: Limit = 10):
    return list(request.app.database.patients.find({}, {"_id": False}, skip=skip, limit=limit))

@patient.get("/{patient_cpf}")
def read_patient(request: Request, patient_cpf: CpfStr):
    return request.app.database.patients.find_one({"cpf": patient_cpf}, {"_id": False})

@patient.put("/{patient_cpf}")
def update_patient(request: Request, patient: PatientUpdate, patient_cpf: CpfStr):
    patient = {k: v for k, v in patient.dict().items() if v is not None}
    if len(patient) >= 1:
        update_result = request.app.database.patients.update_one({"cpf": patient_cpf}, {"$set": patient}).raw_result
        return update_result
    return "wrong format"

@patient.delete("/{patient_cpf}")
def delete_patient(request: Request, patient_cpf: CpfStr):
    return request.app.database.patients.delete_one({"cpf": patient_cpf}).deleted_count