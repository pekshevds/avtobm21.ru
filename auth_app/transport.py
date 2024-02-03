# from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail as send_mail_from_django
from django.conf import settings
from auth_app.services import (
    user_by_username,
    user_by_email
)


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


def check_recipient_function():
    choices = {
        settings.SEND_MESSAGE_TYPE_CHOICES.SMS: user_by_username,
        settings.SEND_MESSAGE_TYPE_CHOICES.EMAIL: user_by_email,
    }
    return choices.get(settings.SEND_MESSAGE_TYPE, None)


def fetch_recipient(recipient: str):
    check_recipient = check_recipient_function()
    return check_recipient(recipient)


def recipient_exist(recipient: str):
    user = fetch_recipient(recipient)
    return user is not None


def send_message(subject: str, message: str, recipient: str):

    """if not recipient_exist(recipient):
        raise ObjectDoesNotExist"""

    transport = transport_function()
    transport(subject=subject,
              message=message,
              recipient_list=[recipient])


def send_pin_code(pin_code: str, recipient: str):
    send_message("auth pin-code", pin_code, recipient)
