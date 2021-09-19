from pydantic import BaseModel


class AppUserBase(BaseModel):
    email: str
    phone: str


class AppUserCreate(AppUserBase):
    comment: str


class AppUser(AppUserBase):
    class Config:
        orm_mode = True
