from sqlalchemy import Column, Integer, String

from app.core.database import Base

class Plant(Base):
    __tablename__ = "plant"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    capacity_kw = Column(Integer, nullable=False)

