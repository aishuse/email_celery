from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from emailcelery import settings


@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"


@shared_task(bind=True)
def send_emails_tasks(self, email, subject, message):
    # import pdb
    # pdb.set_trace()
    users = email.split(",")
    for user in users:
        mail_subject = subject
        message = message
        to_email = user
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"



