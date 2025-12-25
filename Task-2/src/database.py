import psycopg2
import time

def get_connection():
    for attempt in range(5):
        try:
            conn = psycopg2.connect(
                host="postgres",
                port=5432,
                user="postgres",
                password="postgres",
                dbname="mindfuel_db"
            )
            print("Database connection established.")
            return conn
        except psycopg2.OperationalError as e:
            print(f"Database connection failed (attempt {attempt+1}/5): {e}")
            time.sleep(5)
    raise Exception("Could not connect to Postgres after 5 attempts")
