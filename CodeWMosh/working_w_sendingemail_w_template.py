from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path
from string import Template
from tempfile import tempdir

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Syler"
message["to"] = "hello@kishorekumarbehera.com"
message["subject"] = "This is a test email send by python"
body = template.substitute({"name": "john"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("kishore.jpg").read_bytes))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.hello()
    smtp.starttls()
    smtp.login("testuseremail", "testuserpasswd")
    smtp.send_message(message)
    print("Sent...")
