from django.urls import path

#rest
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#my imports
from apps.users.views import UserAPIViewSet

router = DefaultRouter()
router.register('users', UserAPIViewSet, basename="users")


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name = "api_login"),
    path('refresh/', TokenRefreshView.as_view(), name = "api_refresh"),
    
]

urlpatterns += router.urls