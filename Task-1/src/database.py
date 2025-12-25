import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("PGHOST", "postgres"),
        dbname=os.getenv("PGDATABASE", "app_db"),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD", "app_pass"),
        port=os.getenv("PGPORT", "5432")
    )
