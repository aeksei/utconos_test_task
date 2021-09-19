import sys

from fastapi import FastAPI, Depends, Form
from sqlalchemy.orm import Session

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


@app.post("/users/", response_model=schemas.AppUser)
async def create_user(email: str = Form(...),
                      phone: str = Form(...),
                      comment: str = Form(default=""),
                      db: Session = Depends(get_db)):
    user = schemas.AppUserCreate(
        email=email,
        phone=phone,
        comment=comment,
    )

    db_user = crud.create_user(db, user)
    return db_user
