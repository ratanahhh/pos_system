from database import models
from database.db import get_db, engine
from database.models import Base

Base.metadata.create_all(bind=engine)

print("Tables created successfully")