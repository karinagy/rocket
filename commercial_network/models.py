from django.db import models


class CommercialNetwork(models.Model):
    # {0: {"Factory": 564783}, 1: {"IndividualEnerprener": 578844}}
    companies_chain = models.JSONField()

    class Meta:
        verbose_name = 'Торговая сеть'
        verbose_name_plural = 'Торговые сети'
