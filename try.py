import smtplib 
email_server = "smtp.gmail.com:587"
sender = "rahulyup@gmail.com"
to = "rahulyupz@gmail.com"
subject = "How about those Mariners!"
headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (sender, to, subject)
text = "hi"
message = headers + text
mailServer = smtplib.SMTP(email_server)
mailServer.set_debuglevel(1)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login('rahulyup', 'MItocwimon_1&%!@#')
mailServer.ehlo()
mailServer.sendmail(sender, to, message)
mailServer.quit()
