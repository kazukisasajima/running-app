from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from .views import AdminLoginView, UserLoginView
from .views import AdminViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('admins', AdminViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin-login/', AdminLoginView.as_view(), name='admin-login'),
    path('user-login/', UserLoginView.as_view(), name='user-login'),
]