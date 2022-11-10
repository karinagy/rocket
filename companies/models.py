from django.db import models
from django_countries.fields import CountryField

from commercial_network.models import CommercialNetwork
from core.enums.retail_chain_enums import Currency, CompanyTypes
from core.validators import check_lengh_of_chainlink


class Company(models.Model):
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)

    title = models.CharField(validators=[check_lengh_of_chainlink], max_length=255)
    email = models.EmailField()
    country = CountryField()
    # address = AddressField(on_delete=models.CASCADE)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.USD
    )
    company_type = models.CharField(
        max_length=255,
        choices=CompanyTypes.choices
    )

    commercial_network = models.ForeignKey(
        CommercialNetwork,
        verbose_name='торговая сеть',
        on_delete=models.PROTECT,
        related_name='companies',
        null=True,
        blank=True
    )

    purveyor = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title
