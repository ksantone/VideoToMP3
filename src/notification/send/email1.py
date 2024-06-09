import smtplib, os, json
from email.message import EmailMessage

def notification(message):
    print("In notification function of send/email.py")
    try:
        message = json.loads(message)
        mp3_fid = message["mp3_fid"]
        sender_address = os.environ.get("GMAIL_ADDRESS")
        sender_password = os.environ.get("GMAIL_PASSWORD")
        #receiver_address = message["username"]
        receiver_address = "santone.kassim@gmail.com"

        print("Receiver address is: " + receiver_address)
        print("Message parameters created")
        msg = EmailMessage()
        msg.set_content(f"mp3 file_id: {mp3_fid} is now ready!")
        msg["Subject"] = "MP3 Download"
        msg["From"] = sender_address
        msg["To"] = receiver_address

        session = smtplib.SMTP("smtp.gmail.com", 587)
        #session.ehlo()
        session.starttls()
        #session.ehlo()
        print("About to login")
        session.set_debuglevel(1)
        session.login(sender_address, sender_password)
        print("About to send message")
        session.send_message(msg, sender_address, receiver_address)
        session.quit()
        print("Mail Sent")
    except Exception as err:
        print(err)
        return err

