from app.configs.database import db
from sqlalchemy import Column, Integer, VARCHAR
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class AdminsModel(db.Model):

    id: int
    name: str
    last_name: str
    email: str
    username: str

    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    last_name = Column(VARCHAR(50), nullable=False)
    email = Column(VARCHAR(100), unique=True, nullable=False)
    username = Column(VARCHAR(23), unique=True, nullable=False)
    password_hash = Column(VARCHAR(255), nullable=False)


    @property
    def password(self):
        raise AttributeError('Password is not acessible.')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)