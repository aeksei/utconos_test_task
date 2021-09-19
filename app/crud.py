from typing import Optional
from sqlalchemy.orm import Session

from . import models, schemas


def create_user(db: Session, user: schemas.AppUserCreate) -> models.AppUser:
    db_user = models.AppUser(
        phone=user.phone,
        email=user.email,
        comment=user.comment,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_phone(db: Session, phone: str) -> Optional[models.AppUser]:
    return db.query(models.AppUser).filter(models.AppUser.phone == phone).first()


def get_user_by_email(db: Session, email: str) -> Optional[models.AppUser]:
    return db.query(models.AppUser).filter(models.AppUser.email == email).first()
