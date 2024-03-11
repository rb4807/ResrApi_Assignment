from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as rviews
from . import views
from .views import user_logout

router = routers.SimpleRouter()
router.register(r'users', views.CreateUser)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', rviews.obtain_auth_token),
    path('api-logout/', views.user_logout.as_view(), name="api-logout"),
]
