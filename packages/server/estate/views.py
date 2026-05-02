"""Views for estate listings, profiles, saved favorites, and subscriptions."""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

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


# =======================
# HOME
# =======================
def index(request):
    """Render a simple greeting using the first available agent profile."""

    agent = Agent.objects.first()  # pylint: disable=no-member
    name = agent.full_name() if agent else "Guest"
    return HttpResponse(f"Hello, {name}!")


# =======================
# GENERIC LIST VIEW HELPER
# =======================
def render_list(request, model, template, context_name, queryset=None):
    """Render a template with all objects for a model or a provided queryset."""

    data = queryset if queryset is not None else model.objects.all()
    return render(request, template, {context_name: data})


# =======================
# GENERIC DETAIL VIEW HELPER
# =======================
def render_detail(request, model, template, context_name, pk):
    """Render a template with one object looked up by primary key."""

    obj = get_object_or_404(model, id=pk)
    return render(request, template, {context_name: obj})


# =======================
# PROPERTY
# =======================
def property_list(request):
    """Render all property listings."""

    return render_list(
        request,
        Property,
        'estate/property_list.html',
        'properties',
    )


def property_detail(request, property_id):
    """Render one property listing."""

    return render_detail(
        request,
        Property,
        'estate/property_detail.html',
        'property',
        property_id,
    )


# =======================
# AGENT
# =======================
def agent_list(request):
    """Render all agent profiles."""

    return render_list(request, Agent, 'estate/agent_list.html', 'agents')


def agent_detail(request, agent_id):
    """Render one agent profile."""

    return render_detail(
        request,
        Agent,
        'estate/agent_detail.html',
        'agent',
        agent_id,
    )


# =======================
# CLIENT
# =======================
def client_list(request):
    """Render all client profiles."""

    return render_list(request, Client, 'estate/client_list.html', 'clients')


def client_detail(request, client_id):
    """Render one client profile."""

    return render_detail(
        request,
        Client,
        'estate/client_detail.html',
        'client',
        client_id,
    )


# =======================
# INQUIRY
# =======================
def inquiry_list(request):
    """Render all property inquiries."""

    return render_list(request, Inquiry, 'estate/inquiry_list.html', 'inquiries')


def inquiry_detail(request, inquiry_id):
    """Render one property inquiry."""

    return render_detail(
        request,
        Inquiry,
        'estate/inquiry_detail.html',
        'inquiry',
        inquiry_id,
    )


# =======================
# FEATURE
# =======================
def feature_list(request):
    """Render all property features."""

    return render_list(request, Feature, 'estate/feature_list.html', 'features')


def feature_detail(request, feature_id):
    """Render one property feature."""

    return render_detail(
        request,
        Feature,
        'estate/feature_detail.html',
        'feature',
        feature_id,
    )


# =======================
# LOCATION
# =======================
def location_list(request):
    """Render all property locations."""

    return render_list(
        request,
        Location,
        'estate/location_list.html',
        'locations',
    )


def location_detail(request, location_id):
    """Render one property location."""

    return render_detail(
        request,
        Location,
        'estate/location_detail.html',
        'location',
        location_id,
    )


# =======================
# PROPERTY FEATURE
# =======================
def property_feature_list(request):
    """Render all property-feature assignments."""

    return render_list(
        request,
        PropertyFeature,
        'estate/property_feature_list.html',
        'property_features',
    )


def property_feature_detail(request, property_feature_id):
    """Render one property-feature assignment."""

    return render_detail(
        request,
        PropertyFeature,
        'estate/property_feature_detail.html',
        'property_feature',
        property_feature_id,
    )


# =======================
# PROPERTY IMAGE
# =======================
def property_image_list(request):
    """Render all property images."""

    return render_list(
        request,
        PropertyImage,
        'estate/property_image_list.html',
        'property_images',
    )


def property_image_detail(request, property_image_id):
    """Render one property image."""

    return render_detail(
        request,
        PropertyImage,
        'estate/property_image_detail.html',
        'property_image',
        property_image_id,
    )


# =======================
# FAVORITES (USER BASED)
# =======================
@login_required
def favorite_list(request):
    """Render saved favorite properties for the logged-in user."""

    favorites = Favorite.objects.filter(  # pylint: disable=no-member
        user=request.user
    )
    return render(
        request,
        'estate/favorite_list.html',
        {'favorites': favorites},
    )


# =======================
# SUBSCRIPTIONS (USER BASED)
# =======================
@login_required
def subscription_list(request):
    """Render subscriptions for the logged-in agent user."""

    subscriptions = Subscription.objects.filter(  # pylint: disable=no-member
        agent__user=request.user
    )
    return render(
        request,
        'estate/subscription_list.html',
        {'subscriptions': subscriptions},
    )


def subscription_detail(request, subscription_id):
    """Render one subscription."""

    return render_detail(
        request,
        Subscription,
        'estate/subscription_detail.html',
        'subscription',
        subscription_id,
    )
