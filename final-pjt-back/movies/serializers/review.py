from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Review

User = get_user_model()

# 리뷰 작성용
class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('id', 'content', 'score')

# 전체 리뷰 조회용
class ReviewListSerializer(serializers.ModelSerializer):

    class CustomProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username', 'nickname')

    user = CustomProfileSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
