import smtplib
from email.message import EmailMessage

def email_alert(to, subject, body):
    msg= EmailMessage()
    msg.set_content(body)

    msg['subject'] = subject
    msg['to'] = to  
    
    user = "bot.test.2772@gmail.com"
    msg['from'] = user
    password = "aymwnahxqldziueq"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,password)

    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    # email_alert("Michael.crothersmc@gmail.com", "What da word", "ytes is the word")
    email_alert("6366759462@txt.att.net", "What da word", "ytes is the word")
    # email_alert("3145418844@vtext.com", "I can text u from my computer", "helllooooooo priyayyayyaya ayayayaa priya")
