from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.scheduler import get_slots
from backend.email_service import send_email
from backend.google_auth import google_login


app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")



@app.get("/")
def home():

    return FileResponse("frontend/index.html")



@app.post("/login")
def login(data:dict):

    return google_login(data["email"])



@app.get("/slots")
def slots():

    return get_slots()



@app.post("/book")
def book(data:dict):


    send_email(

    data["email"],

    data["date"],

    data["start"],

    data["end"]

    )


    return {"message":"Meeting booked and email sent"}