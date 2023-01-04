from fastapi import FastAPI, Query
import random
from pydantic import BaseModel

app = FastAPI()

class Auto(BaseModel):
    merk: str
    model: str
    horsepower: int
    kleur: str

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

@app.get("/auto/{aantal}/{kleur}")
async def geef_auto(aantal: int, kleur: str):
    aantal_autos = 0
    result = []
    for auto in auto_lijst:
        if auto['kleur'] == kleur:
            result.append(auto)
            aantal_autos += 1
            if aantal_autos >= aantal:
                break
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
