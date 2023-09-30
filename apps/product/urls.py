from django.urls import include, path
from rest_framework import routers
from .views import CompanyViewSet, ProductViewSet, ProductRatingViewSet, CategoryViewSet, SubCategoryViewSet, ApplicationViewSet, QuestionViewSet, GetFilterProductViewSet , PositionViewSet

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-filterGet', GetFilterProductViewSet)
router.register(r'product-ratings', ProductRatingViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'subcategory', SubCategoryViewSet)
router.register(r'position', PositionViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'position', PositionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
