from sqlalchemy.orm import Session
from models import User

def create_user(db: Session, name, course, age):
    db_user=User(name=name,course=course,age=age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.s_id==user_id).first()

def get_users(db: Session):
    return db.query(User).all()

def update_user(db: Session, user_id: int, name: str = None, course: str = None, age: int = None):
    db_user=db.query(User).filter(User.s_id==user_id).first()
    if db_user:
        if name is not None:
            db_user.name = name
        if course is not None:
            db_user.course = course
        if age is not None:
            db_user.age = age
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user=db.query(User).filter(User.s_id==user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
