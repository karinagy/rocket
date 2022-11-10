from rest_framework import serializers

from commercial_network.models import CommercialNetwork
from companies.api.v1.serializers.company import CompanySerializer


class CommercialNetworkSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many=True)

    class Meta:
        model = CommercialNetwork
        fields = ['id', 'companies']
