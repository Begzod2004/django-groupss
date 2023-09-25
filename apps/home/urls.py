from django.urls import include, path
from rest_framework import routers
from .views import  PositionViewSet

router = routers.DefaultRouter()
router.register(r'position', PositionViewSet)


urlpatterns = [
    path('', include(router.urls))
]
