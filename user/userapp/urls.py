from django.db import router
from django.urls import path, include
from .import views
from rest_framework import routers

router=routers.DefaultRouter ()
router.register(r'User',views.UserViewSet,basename='User')
urlpatterns = [
    path ('', include (router.urls))
]