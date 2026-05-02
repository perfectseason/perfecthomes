from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:property_id>/',
         views.property_detail, name='property_detail'),
    path('agents/', views.agent_list, name='agent_list'),
    path('agents/<int:agent_id>/', views.agent_detail, name='agent_detail'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
    path('locations/', views.location_list, name='location_list'),
    path('locations/<int:location_id>/',
         views.location_detail, name='location_detail'),
    path('subscriptions/', views.subscription_list, name='subscription_list'),
    path('subscriptions/<int:subscription_id>/',
         views.subscription_detail, name='subscription_detail'),
    path('property_features/', views.property_feature_list,
         name='property_feature_list'),
    path('property_features/<int:feature_id>/',
         views.property_feature_detail, name='property_feature_detail'),
    path('property_images/', views.property_image_list,
         name='property_image_list'),
    path('property_images/<int:image_id>/',
         views.property_image_detail, name='property_image_detail'),
    path('favorites/', views.favorite_list, name='favorite_list'),
]

