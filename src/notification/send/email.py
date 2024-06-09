from Google import Google
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def notification(message):
    CLIENT_SECRET_FILE = '/app/send/client_secret.json'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    service = Google.Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    print("Service created!")
    emailMsg = 'You won $100,000'
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = 'kubernetes.2000test@gmail.com'
    mimeMessage['subject'] = 'You won'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)
