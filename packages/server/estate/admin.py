"""Django admin configuration for estate app models."""

from django.contrib import admin
from .models import (
    Agent,
    Client,
    Inquiry,
    Location,
    Property,
    PropertyFeature,
    Subscription,
)


class LocationAdmin(admin.ModelAdmin):
    """Admin options for locations."""

    fields = ('country', 'state', 'city', 'address', 'latitude', 'longitude')
    list_display = ('id', 'country', 'state', 'city', 'address')


class AgentAdmin(admin.ModelAdmin):
    """Admin options for agent profiles."""

    list_display = ('id', 'name', 'phone', 'email', 'company')


class ClientAdmin(admin.ModelAdmin):
    """Admin options for client profiles."""

    list_display = ('id', 'name', 'user', 'email', 'phone')


class PropertyAdmin(admin.ModelAdmin):
    """Admin options for property listings."""

    fields = (
        'title',
        'description',
        'price',
        'currency',
        'location',
        'agent',
        'property_type',
        'listing_type',
        'bedrooms',
        'bathrooms',
        'area',
        'is_available',
        'is_featured',
        'video_url',
    )
    list_display = (
        'id',
        'title',
        'price',
        'currency',
        'property_type',
        'listing_type',
        'location',
        'agent',
        'is_available',
    )


class SubscriptionAdmin(admin.ModelAdmin):
    """Admin options for subscriptions."""

    list_display = ('id', 'agent', 'plan', 'start_date', 'end_date', 'is_active')


class PropertyFeatureAdmin(admin.ModelAdmin):
    """Admin options for property feature assignments."""

    list_display = ('id', 'property', 'feature')


class InquiryAdmin(admin.ModelAdmin):
    """Admin options for property inquiries."""

    list_display = ('id', 'name', 'email', 'phone', 'property', 'created_at')


admin.site.register(Location, LocationAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(PropertyFeature, PropertyFeatureAdmin)
admin.site.register(Inquiry, InquiryAdmin)
