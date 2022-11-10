from django.core.exceptions import ValidationError
import datetime


def check_lengh_of_chainlink(value):
    if len(value) > 50:
        raise ValidationError('У объекта сети название должно быть не длиннее 50 символов.')


def check_lengh_of_product(value):
    if len(value) > 25:
        raise ValidationError('У продукта название должно быть не длиннее 25 символов.')


def check_date(value):
    if value > datetime.date.today():
        raise ValidationError('Невозможно указать дату, раньше сегодняшней')
