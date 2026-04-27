from db import engine
from db import Base

Base.metadata.create_all(bind=engine)

print("Tables created")