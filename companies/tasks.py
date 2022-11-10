from celery import shared_task
from random import randint

from .models import Company


@shared_task
def increase_debts():
    for company in Company.objects.all().iterator():
        company.debt += randint(5, 500)
        company.save()


@shared_task
def reduce_debts():
    for company in Company.objects.all().iterator():
        company.debt -= randint(100, 10_000)
        company.save()