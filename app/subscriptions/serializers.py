from rest_framework import serializers
from .models import Subscription


class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

    # 내가 나를 구독할 수 없다. 
    def validate(self, data):
        # data -> request.data를 가리킴
        # datatype(data) : Dict
        if data['subscriber'] == data['subscribed_to']:
            raise serializers.ValidationError('You cannot subsribe to yourself')
        
        return data