from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("djangogramm/", include('djangogramm.urls', namespace='djangogram')),
    path("", include('users.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
