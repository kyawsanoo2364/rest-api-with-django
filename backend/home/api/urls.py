from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("books/", include("books.urls")),
    path("auth/", include("rest_framework.urls")),
    path("auth/", include("authentication.urls")),
    path("auth/token/login/", TokenObtainPairView.as_view()),
    path("auth/token/refresh/", TokenRefreshView.as_view()),
]
