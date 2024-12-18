from app.models import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Date(Base):
    __tablename__ = 'dates'
    id = Column(Integer, autoincrement=True, primary_key=True)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)

    events = relationship('Event', back_populates='date')
