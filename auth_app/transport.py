from django.core.mail import send_mail as send_mail_from_django
from django.conf import settings


def send_sms(subject: str, message: str, recipient_list: []):
    pass


def send_mail(subject: str, message: str, recipient_list: []):
    send_mail_from_django(subject=subject,
                          message=message,
                          from_email=None,
                          recipient_list=recipient_list)


def transport_function():
    choices = {
        settings.SEND_MESSAGE_TYPE_CHOICES.SMS: send_sms,
        settings.SEND_MESSAGE_TYPE_CHOICES.EMAIL: send_mail,
    }
    return choices.get(settings.SEND_MESSAGE_TYPE, None)


def send_message(recipient):
    transport = transport_function()
    transport(subject="pin-code",
              message="pin-code",
              recipient_list=[recipient])
