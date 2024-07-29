from django.urls import path
from . import views

urlpatterns = [
    # Existing URLs
    path('ziprecruiter_generate/', views.ziprecruiter_generate, name='ziprecruiter_generate'),
    path('ziprecruiter_feed/', views.ziprecruiter_feed, name='ziprecruiter_feed'),
    path('jobrapido_generate/', views.jobrapido_generate, name='jobrapido_generate'),
    path('jobrapido_feed/', views.jobrapido_feed, name='jobrapido_feed'),
]
