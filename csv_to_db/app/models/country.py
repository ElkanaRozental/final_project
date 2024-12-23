from app.models import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, autoincrement=True, primary_key=True)
    country = Column(String)

    events = relationship('Event', back_populates='country')
