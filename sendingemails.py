import smtplib
smtp_obj=smtplib.SMTP('smtp.gmail.com',587)
print(smtp_obj.ehlo())

smtp_obj.starttls()

import getpass

email=getpass.getpass("Email:")
password=getpass.getpass("Pasword:")
smtp_obj.login(email,password)

from_address=email
to_address=email
subject=input("Enter the subject line:")
message=input("Enter the body message:")
msg="Subject:"+subject+'\n'+message
smtp_obj.sendmail(from_address,to_address,msg)
smtp_obj.quit()