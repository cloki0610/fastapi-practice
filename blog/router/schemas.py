from dataclasses import dataclass
from sqlite3 import Timestamp
from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    """ Base class for post """
    image_url: str
    title: str
    content: str
    creator: str

class PostDisplay(BaseModel):
    id: int
    image_url: str
    title: str
    content: str
    creator: str
    timestamp: datetime

    class Config():
        orm_mode = True
