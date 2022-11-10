from rest_framework import serializers

from companies.models import Company


class ChainLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
