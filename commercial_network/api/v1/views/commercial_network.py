from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from commercial_network.api.v1.serializers.commercial_network import CommercialNetworkSerializer
from commercial_network.models import CommercialNetwork


# Create your views here.


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class CommercialNetworkViewSet(viewsets.ModelViewSet):
    queryset = CommercialNetwork.objects.all()
    serializer_class = CommercialNetworkSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_class = ChainLinkFilter
    # permission_classes = (IsAdminOrReadOnly,)
    # pagination_class = APIListPagination
    # filter_backends = [DjangoFilterBackend]
    # filter_class =
    # ordering_fields = ['title']
    # search_fields = ['title', 'status']
