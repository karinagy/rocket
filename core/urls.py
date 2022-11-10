from rest_framework.routers import DefaultRouter

from commercial_network.api.v1.views.chain_link_views import ChainLinkMixins, ChainLinkDetailMixins, StatisticsOfDebt
from commercial_network.api.v1.views.commercial_network import CommercialNetworkViewSet
from companies_derevative.api.v1.views.products import ProductViewSet

router = DefaultRouter()
router.register(r'chains_links_update', ChainLinkDetailMixins, basename='chains_links_update')
router.register(r'all_objects', CommercialNetworkViewSet, basename='all_objects')
router.register(r'chains_links', ChainLinkMixins, basename='chains_links')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'chains_links_statistic', StatisticsOfDebt, basename='chains_links_statistic')

urlpatterns = router.urls
