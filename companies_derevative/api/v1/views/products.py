from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from companies_derevative.api.v1.serializers.products import ProductSerializer
from companies_derevative.models import Product
from core.permissions import IsActiveUser


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = (IsActiveUser,)
