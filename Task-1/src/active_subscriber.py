from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

def fetch_user():
    conn = psycopg2.connect(
        host=os.getenv("PGHOST", "postgres"),
        dbname=os.getenv("PGDATABASE", "app_db"),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD", "app_pass"),
        port=os.getenv("PGPORT", "5432"),
    )

    cur = conn.cursor()
    cur.execute("""
        SELECT
                u.user_id,
                u.first_name,
                u.email_address
        FROM users u
        LEFT JOIN email_logs e
        ON u.user_id = e.user_id
        AND e.quote_date = CURRENT_DATE
        WHERE u.subscription_status = 'active'
        AND e.user_id IS NULL;

    """)
    users = cur.fetchall()

    cur.close()
    conn.close()
    return users
