import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import sys
from llm_summary import load_summary


load_dotenv()
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")


def build_email():

    summary = load_summary()

    message = f"""Here is your weekly clincal trials update!:

    {summary}

    """

    msg = MIMEText(message)
    msg["Subject"] = "Daily News for Patrick"
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = GMAIL_ADDRESS

    return msg

def send_email(msg):
    #connect to server
    with smtplib.SMTP("smtp.gmail.com", 587) as con:
        con.starttls()
        con.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        con.sendmail(GMAIL_ADDRESS, GMAIL_ADDRESS, msg.as_string())



if __name__ == "__main__":
    link = sys.argv[1]
    test_msg = build_email(link)
    send_email(test_msg)
    print("Digest email sent")