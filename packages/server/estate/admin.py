"""Django admin configuration for estate app models."""

from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from .models import (
    Agent,
    Client,
    Favorite,
    Feature,
    Inquiry,
    Location,
    Property,
    PropertyFeature,
    PropertyImage,
    Subscription,
)


class ProfileAdminForm(forms.ModelForm):
    """Admin form that edits profile data and linked user identity together."""

    full_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)

    class Meta:
        """Shared admin form options for profile models."""

        fields = ('full_name', 'email', 'phone_number', 'location', 'company')

    def __init__(self, *args, **kwargs):
        """Populate form fields from the profile and linked user."""

        super().__init__(*args, **kwargs)
        user = getattr(self.instance, 'user', None)
        if self.instance.pk and user:
            self.fields['full_name'].initial = self.instance.full_name()
            self.fields['email'].initial = self.instance.email()
            self.fields['phone_number'].initial = self.instance.phone

    def _build_username(self, email):
        """Return a unique username based on the submitted email."""

        base_username = email.split('@', maxsplit=1)[0] or 'user'
        username = base_username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
        return username

    def save(self, commit=True):
        """Save the linked user and profile fields from the admin form."""

        profile = super().save(commit=False)
        full_name = self.cleaned_data['full_name'].strip()
        email = self.cleaned_data['email']
        first_name, _, last_name = full_name.partition(' ')

        user = getattr(profile, 'user', None)
        if user is None or not getattr(user, 'pk', None):
            user = User(username=self._build_username(email))

        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if commit:
            user.save()

        profile.user = user
        profile.phone = self.cleaned_data['phone_number']

        if commit:
            profile.save()
            self.save_m2m()

        return profile


class AgentAdminForm(ProfileAdminForm):
    """Admin form for agent profiles."""

    class Meta(ProfileAdminForm.Meta):
        """Form options for agent profiles."""

        model = Agent


class ClientAdminForm(ProfileAdminForm):
    """Admin form for client profiles."""

    class Meta(ProfileAdminForm.Meta):
        """Form options for client profiles."""

        model = Client


class LocationAdmin(admin.ModelAdmin):
    """Admin options for locations."""

    fields = ('country', 'state', 'city', 'address', 'latitude', 'longitude')
    list_display = ('id', 'country', 'state', 'city', 'address')


class AgentAdmin(admin.ModelAdmin):
    """Admin options for agent profiles."""

    form = AgentAdminForm
    fields = ('full_name', 'email', 'phone_number', 'location', 'company')
    list_display = (
        'id',
        'full_name',
        'email',
        'phone_number',
        'location',
        'company',
    )


class ClientAdmin(admin.ModelAdmin):
    """Admin options for client profiles."""

    form = ClientAdminForm
    fields = ('full_name', 'email', 'phone_number', 'location', 'company')
    list_display = (
        'id',
        'full_name',
        'email',
        'phone_number',
        'location',
        'company',
    )


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


class PropertyImageAdmin(admin.ModelAdmin):
    """Admin options for property images."""

    fields = ('property', 'image', 'is_featured')
    list_display = ('id', 'property', 'image', 'is_featured')


class FeatureAdmin(admin.ModelAdmin):
    """Admin options for property features."""

    fields = ('name',)
    list_display = ('id', 'name')


class SubscriptionAdmin(admin.ModelAdmin):
    """Admin options for subscriptions."""

    fields = ('agent', 'plan', 'start_date', 'end_date', 'is_active')
    list_display = ('id', 'agent', 'plan', 'start_date', 'end_date', 'is_active')


class PropertyFeatureAdmin(admin.ModelAdmin):
    """Admin options for property feature assignments."""

    fields = ('property', 'feature')
    list_display = ('id', 'property', 'feature')


class InquiryAdmin(admin.ModelAdmin):
    """Admin options for property inquiries."""

    fields = ('property', 'name', 'email', 'phone', 'message')
    list_display = ('id', 'name', 'email', 'phone', 'property', 'created_at')


class FavoriteAdmin(admin.ModelAdmin):
    """Admin options for favorite listings."""

    fields = ('user', 'property')
    list_display = ('id', 'user', 'property')


admin.site.register(Location, LocationAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImage, PropertyImageAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(PropertyFeature, PropertyFeatureAdmin)
admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(Favorite, FavoriteAdmin)
