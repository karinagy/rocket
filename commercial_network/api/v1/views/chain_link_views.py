import functools

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins

from rest_framework.viewsets import GenericViewSet

from commercial_network.api.v1.serializers.chain_link_serializer import ChainLinkSerializer
from companies.api.v1.serializers.company import CompanyUpdateSerializer, CompanySerializer
from companies.models import Company
from core.filters.dealership_filter import ChainLinkFilter
from core.permissions import IsActiveUser


class ChainLinkMixins(mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = ChainLinkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ChainLinkFilter


class ChainLinkDetailMixins(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyUpdateSerializer
    permission_classes = (IsActiveUser,)


class StatisticsOfDebt(mixins.ListModelMixin,
                       GenericViewSet):
    qs = Company.objects.all()
    debt_list = []
    for element in qs:
        debt_list.append(element.debt)
    len_of_qs = len(debt_list)
    filtered_list = functools.reduce(lambda x, y: x + y, debt_list)
    averge_qs = filtered_list / len_of_qs
    queryset = Company.objects.filter(debt__gt=averge_qs)
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ChainLinkFilter
    permission_classes = (IsActiveUser,)
