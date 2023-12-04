from django.db.models import Model
from wish_list_app.models import WishList


def fetch_users_wish_list(user: Model) -> [WishList]:
    """Возвращает выборку элементов избранного пользователя user"""
    return WishList.objects.filter(user=user)


def add_to_wish_list(user: Model, good: Model) -> None:
    """Добавляет в избранное пользователя user элемент good"""
    queryset = WishList.objects.filter(user=user, good=good)
    if not queryset:
        WishList.objects.create(user=user, good=good)


def delete_from_wish_list(user: Model, good: Model) -> None:
    """Удаляет из избранного пользователя user элемент good"""
    queryset = WishList.objects.filter(user=user, good=good)
    queryset.delete()


def clear_wish_list(user: Model) -> None:
    """Очищает избранное пользователя user"""
    queryset = WishList.objects.filter(user=user)
    queryset.delete()
