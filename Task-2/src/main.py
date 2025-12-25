from database import get_connection
from extract_quote import extract_quote
from active_subscriber import fetch_user
from send_email import send_email
import csv
import time
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "email_log.csv")

def log_status(email, status, message):
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([email, status, message])

def send_quote_to_users():
    os.makedirs(LOG_DIR, exist_ok=True)

    """ Database connection """
    conn = get_connection()
    cur = conn.cursor()

    """ Fetch Quote """
    quote, author = extract_quote()
    if not quote or not author:
        print("Failed to fetch quote. Exiting.")
        return

    """ Save quote to file """
    QUOTE_FETCHED = os.path.join(LOG_DIR, "quote_fetched.txt")
    with open(QUOTE_FETCHED, "w", encoding="utf-8") as file:
        file.write(f"\"{quote}\" — {author}")
    print(f"Quote saved successfully to {QUOTE_FETCHED}")

    """ Fetch users from database """
    users = fetch_user()
    subject = "Daily Inspirational Quote from MindFuel 🌟"

    for user in users:
        user_id = user[0]   
        name = user[1]      
        email = user[2]    

        message = (
            f"Hi {name},\n\n"
            f"Here is your inspirational quote for today:\n\n"
            f"\"{quote}\" —{author}\n\n"
            f"Have a wonderful and productive day!\n\n"
            f" — MindFuel Team"
        )

        for attempt in range(3):
            success, msg = send_email(email, subject, message)
            if success:
                print(f"Quote sent successfully to {email}")
                log_status(email, "SUCCESS", msg)

                """ Write to database """
                cur.execute("""
                    INSERT INTO email_logs (
                        user_id, 
                        first_name,
                        email_address,
                        quote_date
                    )
                    VALUES (%s, %s, %s, CURRENT_DATE)
                    ON CONFLICT DO NOTHING;
                """, (user_id, name, email))

                conn.commit()
                break
            else:
                print(f"Attempt {attempt + 1} failed for {email}: {msg}")
                time.sleep(5)
        else:
            """ Only runs if all 3 attempts failed """
            log_status(email, "FAILED", msg)
            print(f"Could not send to {email} after 3 attempts.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    send_quote_to_users()
