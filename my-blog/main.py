from fastapi import FastAPI, Depends, Query
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from models import Base, User
import bcrypt

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

# Request body for logging in
class CurrentUser(BaseModel):
    user_input: str # Can be either username or email
    password: str

# Request body for current user (passed to store object, Vuex)
class ReturnUser(BaseModel):
    user_id: int
    user_name: str
    email: str
    

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
    # Hash the password (using bcrypt)
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(user_name=user.user_name, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return True

@app.post("/login")
def login(user: CurrentUser, db: Session = Depends(get_db)):
    matching_user = ''
    
    # Determine whether the user input is a username or email
    if('@' in user.user_input):
        matching_user = db.query(User).filter(User.email == user.user_input).first()
    else:
        matching_user = db.query(User).filter(User.user_name == user.user_input).first()
        
    # Check if the password matches
    if matching_user:
        if bcrypt.checkpw(user.password.encode('utf-8'), matching_user.password):
            return ReturnUser(user_id=matching_user.id, user_name=matching_user.user_name, email=matching_user.email)
        else:
            return False
    else:
        return False