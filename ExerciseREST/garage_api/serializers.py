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
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
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

    def validate(self, attrs: dict) -> dict:
        car_year = attrs.get("year")
        manufacturer = attrs.get("manufacturer")

        # when POST - we DO NOT have an already existing car, so we directly go checking the newly inputed data
        # when PUT - we DO have an already existing car, so we have all needed attributes given
        # when PATCH - we DO have an already existing car, so we check if we have all needed attributes given,
                                            #  if not we extract them from our already existing instance
        if self.instance is not None:
            if car_year is None:
                car_year = self.instance.year
            if manufacturer is None:
                manufacturer = self.instance.manufacturer

        if (
                car_year is not None
                and manufacturer is not None
                and manufacturer.founded_year is not None
                and car_year < manufacturer.founded_year
        ):
            raise serializers.ValidationError(
                {"year": "Cars must be created after the manufacturer has been founded!"},
            )

        return attrs
