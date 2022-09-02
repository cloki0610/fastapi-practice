from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime

class Post(Base):
    """ Data model of posts on the massage board """
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    title = Column(String(255))
    content = Column(String)
    creator = Column(String(50))
    timestamp = Column(DateTime)