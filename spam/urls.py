from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import tafaha
from spam import views
from spam.views import Home

SOCIAL_AUTH_URL_NAMESPACE = 'social'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tests/', include('tafaha.urls')),
    path('', tafaha.views.Home.as_view(), name="home"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('logout/', tafaha.views.Logout.as_view() , name='logout'),
    path('privacy/', views.privacy , name='privacy'),
    path('declaimer/', views.declaimer , name='declaimer'),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
