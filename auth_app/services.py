from django.conf import settings
from django.utils import timezone
from django.db.models.query import QuerySet
from auth_app.models import Pin
from auth_app.models import User


def fetch_find_user_function():
    choices = {
        settings.SEND_MESSAGE_TYPE_CHOICES.SMS: user_by_username,
        settings.SEND_MESSAGE_TYPE_CHOICES.EMAIL: user_by_email,
    }
    return choices.get(settings.SEND_MESSAGE_TYPE, None)


def authenticate(username: str, pincode: str) -> User | None:
    find_user = fetch_find_user_function()
    user = find_user(username)
    if user is not None:
        available_pins = not_used_users_pins(user)
        pincodes = [pin.pin_code for pin in available_pins]
        if pincode in pincodes:
            return user
    return None


def user_by_username(username: str):
    return User.objects.filter(username=username).first()


def user_by_email(email: str):
    return User.objects.filter(email=email).first()


def not_used_users_pins(user: User) -> [Pin]:
    """Возвращает выборку не использовнных пинов пользователя"""
    return Pin.objects.filter(
        user=user,
        use_before__gte=timezone.now(),
        used=False
    )


def users_pin_by_pin_code(
        pins: QuerySet,
        pin_code: str) -> Pin | None:
    """Ищет пин пользователя по пин-коду"""

    for pin in pins:
        if pin.pin_code == pin_code:
            return pin
    return None


def add_pin(user: User) -> Pin:
    """Генерирует пин-код и добавляет его в список
     доступных для пользователя user"""
    pin = Pin(user=user)
    pin.save()
    return pin


def use_pin(pin: Pin) -> Pin:
    """Гасит (делает использованным) pin"""
    pin.used = True
    pin.save()
    return pin
