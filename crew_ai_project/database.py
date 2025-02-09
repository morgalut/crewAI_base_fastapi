import time
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from base import Base  # Import Base from base.py
import models  # Ensure models are imported to register tables

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = "postgresql://admin:admin@localhost:5432/crewai"

# Retry logic for database connection
MAX_RETRIES = 5
WAIT_TIME = 5  # seconds

def get_engine():
    for attempt in range(MAX_RETRIES):
        try:
            engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)
            with engine.connect() as connection:
                logger.info("✅ Successfully connected to the PostgreSQL database!")
            return engine
        except Exception as e:
            logger.warning(f"⚠️  Database connection failed. Retrying in {WAIT_TIME} seconds... (Attempt {attempt+1}/{MAX_RETRIES})")
            time.sleep(WAIT_TIME)
    logger.error("❌ Failed to connect to the database after multiple attempts.")
    return None

engine = get_engine()
if engine:
    Base.metadata.create_all(engine)
    logger.info("✅ Database tables created and ensured!")

# Create a session factory
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
