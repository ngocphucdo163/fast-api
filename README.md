Create .env file, need database credentials at .env

Init
`pip install -r requirements.txt`

`source venv/bin/activate`

1/ Create a create_db.py file in your project directory.

```
from app.database import Base, engine
from app.models import Item  # Import your models here

# Create all tables in the database
print("Creating database schema...")
Base.metadata.create_all(bind=engine)
print("Database schema created!")
```

Run the script:

`python init_db.py`

2/ Run the FastAPI app:

`uvicorn app.main:app --reload`
