from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.models.plant import Plant
from app.schemas.plant import PlantCreate, PlantResponse

route = APIRouter(
    prefix="/plant",
    tags=["plant"],
)

@route.post("/", response_model=PlantResponse)
def create_plant(
        plant: PlantCreate,
        db: Session = Depends(get_db),
):
    db_plant = Plant(**plant.model_dump())

    db.add(db_plant)

    db.commit()

    db.refresh(db_plant)

    return db_plant

