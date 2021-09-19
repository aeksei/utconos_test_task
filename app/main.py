import sys

from fastapi import FastAPI, Depends, Form, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import ValidationError

from app.database import SessionLocal, engine
from app import schemas, crud, models

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}


@app.post("/users/", status_code=status.HTTP_201_CREATED, response_model=schemas.AppUser)
async def create_user(email: str = Form(...),
                      phone: str = Form(...),
                      comment: str = Form(default=""),
                      db: Session = Depends(get_db)):
    try:
        user = schemas.AppUserCreate(
            email=email,
            phone=phone,
            comment=comment,
        )
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))

    db_user = crud.get_user_by_phone(db, user.phone)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Phone already registered")

    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    return crud.create_user(db, user)
