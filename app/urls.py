from django.urls import path, include

from . import views
from rest_framework import routers
from .views import Targets, Blogs, getOneTarget, getOneBlog

app_name = 'app'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('api/target/<int:pk>/health', views.healthCheck, name = 'health'),
    path('api/target/<int:pk>/', getOneTarget.as_view(), name = 'target'),
    path('api/blog/<int:pk>/', getOneBlog.as_view(), name = 'blog'),
]

router = routers.DefaultRouter()
router.register('targets', Targets, basename='targets')
router.register('blogs', Blogs, basename='blogs')
