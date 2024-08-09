import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(".env")


def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create a multipart message
    msg = MIMEMultipart("alternative")
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_email)
    msg['Subject'] = subject

    # Attach message to email
    msg.attach(MIMEText(message, 'plain'))

    # Start the SMTP session
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    try:
        # Login to the SMTP server
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email. Error:", str(e))
    finally:
        # Close the SMTP session
        server.quit()


def send_message(text_msg: list):
    sender = os.getenv("SENDER")
    password = os.getenv("EMAIL_PASSWORD")

    receiver = ['shashank.raj@ondc.org', 'rohit.kumar@scikiq.com', 'pritha.datta@ondc.org', 'ankur.pandey@scikiq.com']
    subject = f"Status update for {datetime.now().strftime('%Y-%m-%d')}"
    message = "\n"

    # for x in text_msg:
    #     message = "\n".join(x)

    for x in text_msg:
        for y in x:
            print(y)
            if y in ["Done", "In Progress", "On Hold", "Delayed", "NA"]:
                print("=" * 20)
                message = message + y + "\n"
                message = message + "========================" + "\n"
            else:
                message = message + y + "\n"

    print("Final Message is", message)
    # Send email

    try:
        send_email(sender, password, receiver, subject, message)
    except Exception as err_main:
        print(err_main.args[0])
    else:
        print("Sending Email was successful.")
