from rest_framework import serializers
from .models import Contest, Security, SecurityPool

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = ('end_date', 'entry_fee', 'num_contestants', 'start_date', 'security_pool_id', 'title')


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = ('last_price', 'price_date', 'security_name', 'ticker')


class SecurityPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityPool
        fields = ('title', 'securities', 'start_price', 'end_price', 'security_pool_id', 'title')