from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str
    phone: str

class UserProfile(BaseModel):
    full_name: str
    email: str
    phone: str
    profile_picture: Optional[str] = None