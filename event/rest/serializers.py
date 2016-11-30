import json

from rest_framework import serializers
from event.models import Event, Url, Site


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event


class UrlSerializer(serializers.ModelSerializer):
    site = serializers.StringRelatedField()

    class Meta:
        model = Url


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
