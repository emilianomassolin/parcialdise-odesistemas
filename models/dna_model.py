from sqlalchemy import Column, Integer, String, Boolean
from database.db_connection import Base

class Dna(Base):
    __tablename__ = 'dna_records'

    id = Column(Integer, primary_key=True)
    dna = Column(String, unique=True, nullable=False)
    mutant_status = Column(Boolean, nullable=False)
