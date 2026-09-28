from dotenv import load_dotenv
import os
from sqlalchemy import URL
from sqlmodel import create_engine,SQLModel,Session


load_dotenv()

USERNAME = os.getenv("DB_NAME")
PASSWORD = os.getenv("DB_PASSWORD")


DB_URL = URL.create(
    drivername="mysql+mysqlconnector",
    username=USERNAME,
    password=PASSWORD,
    host="localhost",
    port=3306,
    database="blog_db"
)

engine = create_engine(
    DB_URL,
    echo=True
)

def create_table():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Session(engine) as session:
        yield session