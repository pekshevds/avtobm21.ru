from django.db import transaction
from catalog_app.models import (
    TradeMark
)


def trade_mark_by_id(tarde_mark_id: str) -> TradeMark:
    return TradeMark.objects.filter(id=tarde_mark_id).first()


def handle_trade_mark(trade_mark_dir: dir) -> TradeMark:
    tarde_mark_id = trade_mark_dir.get('id', "")
    tarde_mark_name = trade_mark_dir.get('name', "")
    trade_mark = trade_mark_by_id(tarde_mark_name)
    if trade_mark is None:
        trade_mark = TradeMark.objects.create(
            id=tarde_mark_id,
            name=tarde_mark_name
        )
    return trade_mark


def handle_trade_mark_list(trade_mark_list: None) -> [TradeMark]:
    tarde_marks_id = []
    with transaction.atomic():
        for trade_mark_item in trade_mark_list:
            trade_mark = handle_trade_mark(trade_mark_dir=trade_mark_item)
            tarde_marks_id.append(trade_mark.id)
    return TradeMark.objects.filter(id__in=tarde_marks_id)
