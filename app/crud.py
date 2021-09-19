from sqlalchemy.orm import Session

from . import models, schemas


def create_user(db: Session, user: schemas.AppUserCreate):
    db_user = models.AppUser(
        phone=user.phone,
        email=user.email,
        comment=user.comment,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
