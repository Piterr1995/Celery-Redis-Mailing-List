from celery import task
from django.core.mail import send_mail


@task
def subscriber_added(email):
    subject = "Thanks for joining XYZ mailing list"
    message = f"We have succesfully added {email} to our mailing list"
    mail_sent = send_mail(subject, message, "x", [email,])
    return mail_sent
