from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as rviews
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.CreateUser)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', rviews.obtain_auth_token),
    path('api-logout/', views.logout),

]
