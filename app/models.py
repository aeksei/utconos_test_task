from sqlalchemy import Column, String

from .database import Base


class AppUser(Base):
    __tablename__ = "app_users"

    email = Column(String, primary_key=True)
    phone = Column(String, nullable=False, unique=True)
    comment = Column(String, nullable=False)
