"""Database models for estate listings and related user activity."""

from urllib import request

from urllib import request

from django.contrib.auth.models import User
from django.db import models


# =======================
# LOCATION MODEL
# =======================
class Location(models.Model):
    """Physical address and coordinates for a property."""

    country = models.CharField(max_length=100, default="Nigeria")
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}, {self.country}"


# =======================
# AGENT MODEL
# =======================
class Agent(models.Model):
    """Real-estate agent profile linked to a Django user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=255, blank=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='agents',
    )

    def full_name(self):
        """Return the linked user's full name."""

        first_name = getattr(self.user, 'first_name', '')
        last_name = getattr(self.user, 'last_name', '')
        return f"{first_name} {last_name}".strip()

    def email(self):
        """Return the linked user's email address."""

        return getattr(self.user, 'email', '')

    def phone_number(self):
        """Return the agent's phone number."""

        return str(self.phone)

    def __str__(self):
        return self.full_name() or str(self.user)


# =======================
# CLIENT MODEL
# =======================
class Client(models.Model):
    """Client profile linked to a Django user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=255, blank=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='clients',
    )

    def full_name(self):
        """Return the linked user's full name."""

        first_name = getattr(self.user, 'first_name', '')
        last_name = getattr(self.user, 'last_name', '')
        return f"{first_name} {last_name}".strip()

    def email(self):
        """Return the linked user's email address."""

        return getattr(self.user, 'email', '')

    def phone_number(self):
        """Return the client's phone number."""

        return str(self.phone)

    def __str__(self):
        return self.full_name() or str(self.user)


# =======================
# PROPERTY MODEL
# =======================
class Property(models.Model):
    """Property listing available for sale, rent, or short let."""

    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('land', 'Land'),
        ('commercial', 'Commercial'),
    ]

    LISTING_TYPES = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
        ('shortlet', 'Short Let'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()

    price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(
        max_length=10,
        default='NGN',
        choices=[
            ('NGN', 'Nigerian Naira'),
            ('USD', 'US Dollar'),
            ('EUR', 'Euro'),
        ]
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='properties'
    )

    agent = models.ForeignKey(
        Agent,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='properties'
    )

    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    listing_type = models.CharField(max_length=20, choices=LISTING_TYPES)

    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Size in sqm"
    )

    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    video_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


# =======================
# PROPERTY IMAGES
# =======================
class PropertyImage(models.Model):
    """Image belonging to a property gallery."""

    property = models.ForeignKey(
        Property,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='property_gallery/')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.property}"


# =======================
# FEATURES
# =======================
class Feature(models.Model):
    """Amenity or feature that can be attached to a property."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class PropertyFeature(models.Model):
    """Join model linking properties to their features."""

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.property} - {self.feature}"


# =======================
# INQUIRIES (LEADS)
# =======================
class Inquiry(models.Model):
    """Lead submitted by a prospective buyer or renter."""

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='inquiries'
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for {self.property}"


# =======================
# FAVORITES
# =======================
class Favorite(models.Model):
    """User-saved property listing."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    class Meta:
        """Model options for saved favorite uniqueness."""

        unique_together = ('user', 'property')

    def __str__(self):
        return f"{self.user} likes {self.property}"


# =======================
# SUBSCRIPTIONS
# =======================
class Subscription(models.Model):
    """Paid plan for an agent."""

    FREE_SUBSCRIPTION = 'F'
    ONE_MONTH_SUBSCRIPTION = 'B'
    SIX_MONTHS_SUBSCRIPTION = 'S'
    ONE_YEAR_SUBSCRIPTION = 'G'

    SUBSCRIPTION_CHOICES = [
        (FREE_SUBSCRIPTION, 'Free'),
        (ONE_MONTH_SUBSCRIPTION, 'Bronze'),
        (SIX_MONTHS_SUBSCRIPTION, 'Silver'),
        (ONE_YEAR_SUBSCRIPTION, 'Gold')
    ]

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    plan = models.CharField(max_length=100)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    subscription = models.CharField(
        max_length=1, choices=SUBSCRIPTION_CHOICES, default='F')

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.agent} - {self.plan}"
