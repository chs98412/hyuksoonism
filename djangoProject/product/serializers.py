from dataclasses import field
from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Product        # product 모델 사용
        fields = '__all__' 

class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserPic
        fields=('title','picture')