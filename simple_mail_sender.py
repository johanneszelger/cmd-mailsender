import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

def send_email(mail_server, port, sender_email, receiver_email, subject, message):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the server and send the email
        with smtplib.SMTP(mail_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls()  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(sender_email, input("Enter your password: "))
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 7:
        print("simple_mail_sender mail_server port sender_email receiver_email subject message")
    else:
        send_email(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
