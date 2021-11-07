from rest_framework import serializers
from .models import Contest, Security, SecurityPool

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = ('title', 'start_date', 'end_date', 'entry_fee', 'num_contestants',
                  'secpool_id', 'sec_start_price', 'sec_end_price')


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = ('last_price', 'price_date', 'security_name', 'ticker')


class SecurityPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityPool
        fields = ('title', 'security')
