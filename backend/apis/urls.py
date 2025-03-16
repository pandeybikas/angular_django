from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'water/study', views.ProjectMainViewSetClass, basename='water_study')

urlpatterns= [
    path('api/', include(router.urls))
]