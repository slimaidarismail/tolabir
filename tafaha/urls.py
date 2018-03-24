from django.urls import path, include

from tafaha.views import Home, SingleTest, Loading, Result

urlpatterns = [
    path('', Home.as_view(), name = "home_page"),
    path('<int:id>', SingleTest.as_view(), name="single-test"),
    path('loading/<int:id>', Loading.as_view(), name="loading"),
    path('reasults/<int:id>', Result.as_view(), name="result"),
]