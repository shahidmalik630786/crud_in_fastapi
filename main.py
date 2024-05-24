
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Base, engine
from crud import get_blog, create_blog, get_all_blog,delete_blog,update_blog,create_user_query,get_all_user
from dependencies import get_db
from schemas import Blog,ShowBlog,User,ShowUser
from typing import List


app = FastAPI()

# Initialize the database
Base.metadata.create_all(bind=engine)




#create
@app.post("/blogcreate/",tags=['blogs'])
def create_user_endpoint(title: str, body: str, user_id:int ,db: Session = Depends(get_db)):
    return create_blog(db, title, body,user_id)

# retrieve specific blog
@app.get("/blog/{id}", response_model=ShowBlog,tags=['blogs'])
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = get_blog(db, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

#retrive all blog
@app.get("/allblog/", response_model=List[Blog],tags=['blogs'])
def read_users(db: Session = Depends(get_db)):
    return get_all_blog(db)

#update
@app.put("/blogupdate/{id}",tags=['blogs'])
def update_blog_endpoint(id: int, title: str, body: str, db: Session = Depends(get_db)):
    updated_blog = update_blog(db, id, title, body)
    if updated_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return updated_blog


#delete
@app.delete("/blogdelete/{id}",tags=['blogs'])
def delete_blog_endpoint(id: int, db: Session = Depends(get_db)):
    deleted = delete_blog(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": "Blog deleted successfully"}


#create user
@app.post('/user',tags=['user'])
def create_user(request:User, db: Session = Depends(get_db)):
    return create_user_query(db,request.name,request.email,request.password)

#retrive all users
@app.get('/alluser/',response_model=List[ShowUser],tags=['user'])
def all_users(db: Session = Depends(get_db)):
    return get_all_user(db)