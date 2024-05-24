from sqlalchemy.orm import Session
from models import Blog, User
from hashing import hashed_password


def get_blog(db: Session, id: int):
    print(id,"************************")
    print(db.query(Blog).filter(Blog.id == id).first(),"************************")
    return db.query(Blog).filter(Blog.id == id).first()

def create_blog(db: Session, title: str, body: str,user_id:int):
    db_blog = Blog(title=title, body=body,user_id=user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def get_all_blog(db: Session):
    return db.query(Blog).all()


def update_blog(db: Session, id: int, title: str, body: str):
    db_blog = get_blog(db, id)
    if db_blog:
        db_blog.title = title
        db_blog.body = body
        db.commit()
        db.refresh(db_blog)
        return db_blog
    return None

def delete_blog(db: Session, id: int):
    print(id,"**************")
    db_blog = get_blog(db, id)
    print(db_blog,"*********")
    if db_blog:
        db.delete(db_blog)
        db.commit()
        return True
    return False





def create_user_query(db: Session,name: str,email: str,password: str):
    hash_password = hashed_password(password)
    db_user = User(name=name,email=email,password=hash_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_user(db: Session):
    return db.query(User).all()