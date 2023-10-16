from typing import Union, Annotated

from fastapi import FastAPI, Path
import models
import database
import domain
from uuid import UUID

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


## TODO chybi strankovani
@app.get("/pets")
def get_pets() -> list[models.Pet] | None:
    pets = database.SessionLocal.begin().query(domain.Pet)
    return [
        models.Pet(**p) ##  rozbal je do modelu pet
        for p in pets ## nacti pets a ^
    ]

@app.get("/pet/{pet_id}")
def get_pet(pet_id: Annotated[UUID, Path(title="Pet's id")]) -> models.Pet:
    return pet_id