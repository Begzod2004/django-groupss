from django.urls import include, path
from rest_framework import routers
from .views import CompanyViewSet, ProductViewSet, ProductRatingViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-ratings', ProductRatingViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
