from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('listings/', include('listings.urls')),
    path('contacts/', include('contacts.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
