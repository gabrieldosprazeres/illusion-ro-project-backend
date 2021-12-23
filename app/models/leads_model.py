from app.configs.database import db
from sqlalchemy import Column, Integer, VARCHAR, DateTime
from dataclasses import dataclass
from datetime import datetime


@dataclass
class LeadsModel(db.Model):

    id: int
    name: str
    last_name: str
    email: str
    phone: str
    username: str
    created_at: str

    __tablename__ = 'leads'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    last_name = Column(VARCHAR(50), nullable=False)
    email = Column(VARCHAR(100), unique=True, nullable=False)
    phone = Column(VARCHAR(15), unique=True, nullable=False)
    username = Column(VARCHAR(23), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())