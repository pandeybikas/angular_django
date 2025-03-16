from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'sample/test', views.ProjectMainViewSetClass, basename='testing')

urlpatterns= [
    path('api/', include(router.urls))
]