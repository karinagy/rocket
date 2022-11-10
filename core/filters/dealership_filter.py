from django_filters import rest_framework as filters

from companies.models import Company


class ChainLinkFilter(filters.FilterSet):
    commercial_network = filters.NumberFilter()
    country = filters.CharFilter()
    products = filters.NumberFilter(field_name='products__id')

    class Meta:
        model = Company
        fields = ['commercial_network', 'country', 'products']
