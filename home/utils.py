from home.models import Student
import time
from django.core.mail import send_mail
from django.conf import settings

def dependent_function():
    print("Function Started!")
    time.sleep(1)
    print("Function Executed!")

#   In this file,if it is dependent on some other files,modals like Student ...we can't 
#   directly call this,as it will give error from right run icon...
#   We need to import it in shell ,then call this function...
#   e.g. In shell-> from home.utils import *  -> then dependent_function() 
    
def send_email_to_client():
    subject="Highly confidential email from Ministry of #SHAYAMA_JI_SARKAR✅🚩"
    message="SMILE IN ALL SITUATIONS! #HARE KRISHNA!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list=[""]

    send_mail(subject,message,from_email,recipient_list)