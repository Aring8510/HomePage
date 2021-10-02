from django.urls import path, include

from . import views
from rest_framework import routers
from .views import Targets

app_name = 'app'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('device/<int:pk>/health', views.healthCheck, name = 'health'),
]

router = routers.DefaultRouter()
router.register('targets', Targets, basename='target')
