from django.contrib.auth.models import User, Group
from rest_framework import serializers
from catalog import models


class SerializerCountry(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'


class SerializerProvince(serializers.ModelSerializer):
    class Meta:
        model = models.Province
        fields = '__all__'


class SerializerCity(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class SerializerAttraction(serializers.ModelSerializer):
    class Meta:
        model = models.Attraction
        fields = '__all__'


class SerializerPlan(serializers.ModelSerializer):
    geo_dist = serializers.FloatField()

    class Meta:
        model = models.Plan
        fields = ['id', 'present_id', 'all_days', 'cost_rate', 'geo_dist']


class SerializerPlan_details(serializers.ModelSerializer):

    class Meta:
        model = models.PlanDetails
        fields = '__all__'


class SerializerPlan_details_full(serializers.ModelSerializer):
    plan_details = SerializerPlan_details()
    attraction = SerializerAttraction()

    class Meta:
        model = models.PlanDetails
        fields = ('plan_details', 'attraction')

