import smtplib

email = input("SENDER EMAIL:")
receiver_email = input("RECEIVER EMAIL: ")

subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
#starting ls for serverserver

server.login(email, "oivuxrausglmretq")
#login to the server. using app password to ologin to email 

server.sendmail(email, receiver_email, text)
# send email to receiver email

print("Email has been sent to" + receiver_email)