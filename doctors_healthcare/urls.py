
from django.contrib import admin
from django.urls import path
from texts.views import home
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from texts.views import home, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)