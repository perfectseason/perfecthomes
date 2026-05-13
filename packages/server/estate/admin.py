"""Django admin configuration for estate app models."""

from django.contrib import admin, messages
from django import forms
from django.utils.html import format_html, urlencode
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


class InventoryFilter(admin.SimpleFilter):
    title = 'property'
    parameter_name = 'property'

    def lookups(self, request, model_admin):
        return [
            ('<1', 'Unavailable')
            ('>0', 'Available')
        ]

    def queryset(self, request, quesryset: Queryset):
        if self.value() == '<1', '>0':
            return queryset.filter(inventory_lt=1, inventory_gt=0)



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
    search_fields = ['first_name__istartwith']


class PropertyImageInline(admin.TabularInline):
    model = models.ProductImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ''


@admin.register(models.Product)
class PropertyAdmin(admin.ModelAdmin):
    """Admin options for property listings.
    actions = ['clear_inventory']
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
    inlines = [ProductImageInline]
    list_display = (
        'id',
        'title',
        'price',
        'currency',
        'property_type',
        'listing_type',
        'Inventory_Filter'
        'location',
        'agent',
        'is_available',
    )



    @admin.action(description='Clear property')
    def clear_property(self, request, queryset):
        updated_count = queryset.update(property=0)
        self.message_user(
            request,
            f'{updated_count} property were succesfully updated.'
            message.ERROR
        )

    ordering = ['first_name', 'last_name']
    search_fields = ['property__istartwith', 'location__istartwith']

    @admin.display(description='Agent')
    class inventory_status(admin.SimpleListFilter):
        # """Custom filter for property availability."""

        title = 'Inventory Status'
        parameter_name = 'inventory_status'

        def lookups(self, request, model_admin):
            """Return filter options for inventory status."""

            return (
                ('available', 'Available'),
                ('unavailable', 'Unavailable'),
            )

        def queryset(self, request, queryset):
            """Filter properties based on selected inventory status."""

            if self.value() == 'available':
                return queryset.filter(is_available=True)
            elif self.value() == 'unavailable':
                return queryset.filter(is_available=False)
            return queryset


        class media:
            css = {
                 'all': ['estate/style.css']
            }


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
    search_fields = ['property__istartwith', 'location__istartwith']


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
