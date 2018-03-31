from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import tafaha
from spam.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tests/', include('tafaha.urls')),
    path('', tafaha.views.Home.as_view(), name="home"),
    # path('auth/social', Home.as_view(), name="auth-social"),
    # path('auth-social', include('social_django.urls', namespace="social")),
    path('accounts/', include('allauth.urls')),

    path('', Home.as_view(), name="logout")

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

LOGIN_REDIRECT_URL = "home"