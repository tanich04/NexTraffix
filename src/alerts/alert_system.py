import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Email configuration
SENDER_EMAIL = "your_email@example.com"
SENDER_PASSWORD = "your_password"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
RECIPIENT_EMAIL = "law_enforcement@example.com"

# Logging setup
logging.basicConfig(filename='alerts.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def send_alert(subject, body):
    """Send an email alert to law enforcement."""
    try:
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = SENDER_EMAIL
        message['To'] = RECIPIENT_EMAIL
        message['Subject'] = subject

        # Attach the body with the email
        message.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            text = message.as_string()
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, text)

        logging.info(f"Alert sent: {subject}")
    except Exception as e:
        logging.error(f"Error sending alert: {e}")

def generate_alert(post_details):
    """Generate and send an alert for suspicious activity."""
    post_content = post_details.get('content', 'No content available')
    post_type = post_details.get('type', 'Unknown')
    user_id = post_details.get('user_id', 'Unknown')
    
    subject = f"Suspicious Activity Detected: {post_type} by User {user_id}"
    body = f"""
    A suspicious post was detected on the platform. Below are the details:

    Post Type: {post_type}
    User ID: {user_id}
    Content: {post_content}

    Please review the post and take appropriate action.

    -- Automated Alert System
    """

    send_alert(subject, body)

# Example usage
if __name__ == "__main__":
    suspicious_post = {
        "content": "Buy synthetic drugs now!",
        "type": "Text",
        "user_id": "user123"
    }
    
    generate_alert(suspicious_post)
