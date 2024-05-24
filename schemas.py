from pydantic import BaseModel
from typing import List


class ShowBlog (BaseModel):
    title: str
    body: str
    user_id: int

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    id: int
    name: str
    email: str


class Blog (BaseModel):
    title: str
    body: str
    user_id: int
    creator : ShowUser
    
class ShowUserextended(ShowUser):
    blogs: List[Blog]=[]
    
    class Config:
        orm_mode = True