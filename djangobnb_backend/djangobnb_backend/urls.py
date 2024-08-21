from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .admin_site import admin_site  # Import the custom AdminSite

urlpatterns = [
    path('admin/', admin_site.urls),  # Use the custom AdminSite
    path('api/properties/', include('property.urls')),
    path('api/properties/<uuid:property_id>/', include('review.urls')),  # Include review URLs under properties
    path('api/auth/', include('useraccount.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/community/', include('community.urls')),  # Include community URLs
    path('api/payments/', include('payments.urls')),  # Include payment URLs here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
