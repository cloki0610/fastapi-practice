import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.models import Post
from router.schemas import PostBase

def create_post(db: Session, request: PostBase):
    """ Controller function for create a new post """
    new_post = Post(
        image_url = request.image_url,
        title = request.title,
        content = request.content,
        creator = request.creator,
        timestamp = datetime.datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_post(db: Session):
    """ Controller function for get all posts """
    return db.query(Post).all()

def delete_post(id:int, db: Session):
    """ Controller function for delete a post """
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} does not exist")
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully."}
