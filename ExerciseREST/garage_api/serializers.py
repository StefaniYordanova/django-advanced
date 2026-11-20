from rest_framework import serializers
from .models import Manufacturer, Car

"""
Serializer -> we need to implement 
the create() and update() methods, because when 
using save() in the views create() or update() are called
"""
class ManufacturerSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=20,
    )

    country = serializers.CharField(
        max_length=10,
    )

    def create(self, validated_data):
        return Manufacturer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.country = validated_data.get('country')
        instance.save()
        return instance


# OR we can use ModelSerializer where we do not need to override create() and update() methods
class ManufacturerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
