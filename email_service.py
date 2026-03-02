import smtplib


EMAIL="hibasaeed424@gmail.com"

PASSWORD="cyynjjycdyaevmhb"



def send_email(to,date,start,end):


    message=f"""

AI Smart Meeting Scheduler

Meeting Confirmed


Date:{date}

Time:{start}-{end}

"""


    server=smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login(EMAIL,PASSWORD)

    server.sendmail(EMAIL,to,message)

    server.quit()