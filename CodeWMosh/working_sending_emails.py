from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path

message = MIMEMultipart()
message["from"] = "Syler"
message["to"] = "hello@kishorekumarbehera.com"
message["subject"] = "This is a test email send by python"
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("kishore.jpg").read_bytes))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.hello()
    smtp.starttls()
    smtp.login("testuseremail", "testuserpasswd")
    smtp.send_message(message)
    print("Sent...")
