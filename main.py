from fastapi import FastAPI
from pydantic import BaseModel

fast = FastAPI()


class Notes(BaseModel):
    francais: int
    math: float
    anglais : float
    description: str

@fast.get("/ici/")
def get_home():
    return {"message": "a demain"}

@fast.get("/notes/")
def get_notes(notes: Notes):
    return {"notes": notes}

@fast.post("/abb/")
def post_notes(notes: Notes):
    return notes
    