import smtplib
my_email = "hr326157@gmail.com"
PASWORD = "unlrxswjkctvnucn"

with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
    #Transport layer security
    connect.starttls()
    connect.login(user=my_email, password=PASWORD)
    connect.sendmail(from_addr=my_email, 
                    to_addrs="elalvaro@yahoo.com", 
                    msg="Subject: TEST PY\n\nHola pa"
                    )
 