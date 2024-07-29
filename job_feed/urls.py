from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from jobs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls')),  # Routes to job-related URLs
    path('', views.home, name='home'),    # The root URL should route to the home view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
