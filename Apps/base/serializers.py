from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from .models import (
    Department,
    Router,
    Country,
    Province,
    City,
    Area,
    Town
)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add extra responses here
        data['nickname'] = self.user.userinfo.nickname if self.user.userinfo else ""
        data['dep_name'] = self.user.userinfo.dep.name if self.user.userinfo.dep else "" if self.user.userinfo else ""
        data['groups'] = self.user.groups.values_list('name', flat=True)
        # data['permissions'] = self.user.get_all_permissions()
        return data


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ('id',)


class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=True, max_length=90)

    def create(self, validated_data):
        """Create a new "country" instance"""
        return Country.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Use validated data to return an existing `country` instance。"""
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = '__all__'
        read_only_fields = ('id',)


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'
        read_only_fields = ('id',)


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = '__all__'
        read_only_fields = ('id',)


class TownSerializer(serializers.ModelSerializer):

    class Meta:
        model = Town
        fields = '__all__'
        read_only_fields = ('id',)
