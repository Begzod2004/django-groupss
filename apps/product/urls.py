from django.urls import include, path
from rest_framework import routers
from .views import CompanyViewSet, ProductViewSet, ProductRatingViewSet, CategoryViewSet, SubCategoryViewSet

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-ratings', ProductRatingViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'subcategory', SubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
