from fastapi import FastAPI, Depends, HTTPException
import random
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import auth

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:63342",
    "http://127.0.0.1:63342",
    "https://system-service-mathieudj.cloud.okteto.net/",
    "https://system-service-mathieudj.cloud.okteto.net/auto/",
    "https://system-service-mathieudj.cloud.okteto.net/auto",
    "https://transcendent-syrniki-fe2fcd.netlify.app",
    "https://mathieu2002.github.io/",
    "https://mathieu2002.github.io",
    "https://mathieu2002.github.io."
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Auto(BaseModel):
    merk: str
    model: str
    horsepower: int
    kleur: str


class Horsepower(BaseModel):
    horsepower: int


auto_lijst = [
    {
        "merk": "Mercedes-Benz",
        "model": "S-Class",
        "horsepower": 362,
        "kleur": "zwart"
    },
    {
        "merk": "BMW",
        "model": "7 Series",
        "horsepower": 335,
        "kleur": "zilver"
    },
    {
        "merk": "Audi",
        "model": "A8",
        "horsepower": 335,
        "kleur": "grijs"
    },
    {
        "merk": "Tesla",
        "model": "Model S",
        "horsepower": 760,
        "kleur": "wit"
    },
    {
        "merk": "Lexus",
        "model": "LS",
        "horsepower": 416,
        "kleur": "blauw"
    },
    {
        "merk": "Acura",
        "model": "NSX",
        "horsepower": 573,
        "kleur": "rood"
    },
    {
        "merk": "Ford",
        "model": "Mustang",
        "horsepower": 460,
        "kleur": "geel"
    },
    {
        "merk": "Chevrolet",
        "model": "Corvette",
        "horsepower": 495,
        "kleur": "groen"
    },
    {
        "merk": "Dodge",
        "model": "Challenger",
        "horsepower": 717,
        "kleur": "oranje"
    },
    {
        "merk": "Nissan",
        "model": "GT-R",
        "horsepower": 565,
        "kleur": "paars"
    },
    {
        "merk": "Mitsubishi",
        "model": "Lancer Evo",
        "horsepower": 291,
        "kleur": "geel"
    },
    {
        "merk": "Subaru",
        "model": "WRX STI",
        "horsepower": 310,
        "kleur": "rood"
    },
    {
        "merk": "Honda",
        "model": "Civic Type R",
        "horsepower": 306,
        "kleur": "groen"
    },
    {
        "merk": "Hyundai",
        "model": "Veloster N",
        "horsepower": 275,
        "kleur": "geel"
    },
    {
        "merk": "Kia",
        "model": "Stinger",
        "horsepower": 365,
        "kleur": "blauw"
    },
    {
        "merk": "Mazda",
        "model": "Miata",
        "horsepower": 181,
        "kleur": "grijs"
    },
    {
        "merk": "Mini",
        "model": "Cooper S",
        "horsepower": 189,
        "kleur": "zwart"
    },
    {
        "merk": "Peugeot",
        "model": "308 GTI",
        "horsepower": 250,
        "kleur": "blauw"
    },
    {
        "merk": "Renault",
        "model": "Megane RS",
        "horsepower": 296,
        "kleur": "rood"
    },
    {
        "merk": "Skoda",
        "model": "Octavia RS",
        "horsepower": 245,
        "kleur": "wit"
    }
]


@app.get("/auto/{aantal}")
async def geef_auto(aantal: int = 5):
    if aantal > len(auto_lijst):
        aantal = len(auto_lijst)
    elif aantal < 0:
        return {"foutmelding": "Het aantal auto's moet een positief getal zijn."}
    willekeurige_auto_lijst = random.sample(auto_lijst, aantal)
    return willekeurige_auto_lijst


@app.get("/auto/")
async def geef_auto():
    willekeurige_auto_lijst = random.sample(auto_lijst, 5)
    return willekeurige_auto_lijst


@app.get("/auto/kleur/{kleur}")
async def geef_auto_kleur(kleur: str):
    result = []
    for auto in auto_lijst:
        if auto["kleur"] == kleur:
            result.append(auto)
    return result


@app.get("/auto/horsepower/{min_horsepower}/{max_horsepower}")
async def geef_auto_horsepower(min_horsepower: int, max_horsepower: int):
    result = []
    for auto in auto_lijst:
        if min_horsepower <= int(auto["horsepower"]) <= max_horsepower:
            result.append(auto)
    return result


@app.post("/auto/")
async def voeg_auto_toe(auto: Auto):
    auto_lijst.append(auto.dict())
    return {"message": "Auto toegevoegd aan lijst"}


@app.delete("/auto/{merk}")
async def verwijder_auto(merk: str):
    nieuwe_lijst = [auto for auto in auto_lijst if auto["merk"] != merk]
    auto_lijst.clear()
    auto_lijst.extend(nieuwe_lijst)
    return {"message": f"Auto's met merk {merk} verwijderd"}


@app.put("/auto/{merk}/{model}")
async def update_auto(merk: str, model: str, auto: Horsepower):
    for a in auto_lijst:
        if a["merk"] == merk and a["model"] == model:
            a["horsepower"] = auto.horsepower
            return {"status": "success"}
    return {"status": "not found"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
   
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

