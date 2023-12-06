from django.db.models import Model
from cart_app.models import Cart


def fetch_users_cart(user: Model) -> [Cart]:
    """Возвращает выборку элементов корзины пользователя user"""
    return Cart.objects.filter(user=user)


def add_to_cart(user: Model, good: Model, quantity: float = 1) -> None:
    """Добавляет в корзину пользователя user элемент good"""
    record = Cart.objects.filter(user=user, good=good).first()
    if not record:
        Cart.objects.create(user=user, good=good, quantity=quantity)
    else:
        record.quantity += quantity
        record.save()


def delete_from_cart(user: Model, good: Model, quantity: float = 1) -> None:
    """Удаляет из корзины пользователя user элемент good"""
    record = Cart.objects.filter(user=user, good=good).first()
    if record:
        if quantity >= record.quantity:
            record.delete()
        else:
            record.quantity -= quantity
            record.save()


def clear_cart(user: Model) -> None:
    """Очищает корзину пользователя user"""
    queryset = Cart.objects.filter(user=user)
    queryset.delete()
