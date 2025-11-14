import psycopg2
from psycopg2.extras import RealDictCursor
from app.server.dependencies import get_settings

settings = get_settings()

def get_db_connection():
    conn = psycopg2.connect(
        dbname=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        cursor_factory=RealDictCursor
    )
    return conn