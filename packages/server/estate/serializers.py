"""Serializers for estate API endpoints."""

from rest_framework import serializers

from .models import (
    Agent,
    Client,
    Favorite,
    Location,
    Property,
    PropertyFeature,
    PropertyImage,
    Subscription,
)


class LocationSerializer(serializers.ModelSerializer):
    """Serialize property locations."""

    class Meta:
        model = Location
        fields = "__all__"


class AgentSerializer(serializers.ModelSerializer):
    """Serialize real-estate agents."""

    class Meta:
        model = Agent
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    """Serialize client profiles."""

    class Meta:
        model = Client
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):
    """Serialize property listings."""

    class Meta:
        model = Property
        fields = "__all__"


class PropertyImageSerializer(serializers.ModelSerializer):
    """Serialize property gallery images."""

    class Meta:
        model = PropertyImage
        fields = "__all__"


class PropertyFeatureSerializer(serializers.ModelSerializer):
    """Serialize property-feature assignments."""

    class Meta:
        model = PropertyFeature
        fields = "__all__"


class FavoriteSerializer(serializers.ModelSerializer):
    """Serialize saved favorite properties."""

    class Meta:
        model = Favorite
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    """Serialize agent subscriptions."""

    class Meta:
        model = Subscription
        fields = "__all__"
