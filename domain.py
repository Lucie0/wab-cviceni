from sqlalchemy import UUID, Boolean, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

class Bed(Base):
    __tablename__ = "beds"

    id = Column(UUID, primary_key=True, index=True, unique=True)
    type = Column(String)
    

class MedicalExamination(Base):
    __tablename__ = "medical_examinations"

    id = Column(UUID, primary_key=True, index=True, unique=True)
    datetime = Column(DateTime, nullable=False)
    doctor = Column(String)
    report = Column(String)
    pet_id = Column(UUID, ForeignKey("pets.id"))
    

class Pet(Base):
    __tablename__ = "pets"

    id = Column(UUID, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    registration_date = Column(DateTime, nullable=False)
    bed = relationship("Bed")
    medical_examination = relationship("MedicalExamination")