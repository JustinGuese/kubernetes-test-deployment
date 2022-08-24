from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db, UserDB, User
from typing import List


app = FastAPI(title= "TEST User Api", version = "2.0.1")

@app.get("/user/{username}", response_model=User)
async def get_user(username: str, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return User(**user.__dict__)

@app.post("/user/", status_code=201)
async def create_user(user: User, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    db_user = UserDB(**user.dict())
    db.add(db_user)
    db.commit()

@app.get("/users/", response_model=List[User])
async def get_users(limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(UserDB).limit(limit).all()
    return [User(**user.__dict__) for user in users]