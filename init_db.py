from app.database import Base, engine
from app.models import Item 

# Create all tables in the database
print("Creating database schema...")
Base.metadata.create_all(bind=engine)
print("Database schema created!")