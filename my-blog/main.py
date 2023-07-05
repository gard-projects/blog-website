from fastapi import FastAPI, Depends, Query
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from models import Base, User

# Connection string (SQLAlchemy uses it to connect to the database)
DATABASE_URL = "sqlite:///./my-blog.db"

# Create engine object (knows how to interact with the database)
engine = create_engine(DATABASE_URL)

# Create Session objects (used for making queries to database)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables, and use the engine to connect to the database
Base.metadata.create_all(bind=engine)

# Request body for creating a new user
class NewUser(BaseModel):
    user_name: str
    email: str
    password: str

# Create FastAPI instance
app = FastAPI()

# Function that provides a unique database session for each request (and closes the session afterwards)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Check if username is in use (upon account registration)
@app.get("/check_username")
def check_username(user_name: str, db: Session = Depends(get_db)):
    matching_user = db.query(User).filter(User.user_name == user_name).first()
    print(matching_user)
    if matching_user:
        return True
    else:
        return False

# Check if email is in use (upon account registration)
@app.get("/check_email")
def check_email(email: str, db: Session = Depends(get_db)):
    email = db.query(User).filter(User.email == email).first()
    if email:
        return True
    else:
        return False
    
@app.post("/register_user")
def register_user(user: NewUser, db: Session = Depends(get_db)):
    new_user = User(user_name=user.user_name, email=user.email, password=user.password)
    print(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return True