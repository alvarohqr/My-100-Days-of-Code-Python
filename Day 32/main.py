import smtplib
import datetime as dt

# my_email = "hr326157@gmail.com"
# PASWORD = "unlrxswjkctvnucn"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
#     #Transport layer security
#     connect.starttls()
#     connect.login(user=my_email, password=PASWORD)
#     connect.sendmail(from_addr=my_email, 
#                     to_addrs="elalvaro@yahoo.com", 
#                     msg="Subject: TEST PY\n\nHola pa"
#                     )

now = dt.datetime.now()
year = now.year

date_of_birth = dt.datetime(year=1995, month=12, day=13, hour=11, minute=13)
print(date_of_birth) 