from pydantic import BaseModel

class PlantCreate(BaseModel):
    name: str
    location: str
    capacity_kw: int

class PlantResponse(BaseModel):
    id: int

    class Config:
        from_atributes = True
