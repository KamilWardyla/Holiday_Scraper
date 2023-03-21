import smtplib
import ssl
from email.message import EmailMessage
from localsettings import email_sender_settings, email_password_settings

def email_sender(text, link):
    # Login data
    email_sender = email_sender_settings
    email_password = email_password_settings
    email_receiver = 'conax13@gmail.com'
    # Email data
    subject = 'Nowa Promka Na Wakacje'
    body = f"""
    Promocja 
    Text: {text}
    Link: {link}
    """
    # Crate EmailMessage class
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    # Login and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    return "Wiadomość wysłana"
