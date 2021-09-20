from pydantic import BaseModel, EmailStr


class AppUserBase(BaseModel):
    email: EmailStr
    phone: str


class AppUserCreate(AppUserBase):
    comment: str


class AppUser(AppUserBase):
    class Config:
        orm_mode = True
