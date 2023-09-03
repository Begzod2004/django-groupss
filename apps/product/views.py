
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework import viewsets, filters
from rest_framework.response import Response

from .serializers import CompanySerializer, ProductSerializer, ProductRatingSerializer, ProductRetrieveSerializer, SubCategorySerializer, ApplicationSerializer, QuestionSerializer
from .models import Company, Product, ProductRating, SubCategory, Application, Question
from .filters import ProductFilter
from rest_framework.filters import SearchFilter
from .models import Category
from rest_framework import viewsets, status
from django.db.models import F
from .serializers import CategorySerializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

class GetCSRFToken(views.APIView):
    permission_classes = [AllowAny, ]

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, format=None):
        return Response("Success")




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'head', 'options']

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    # Add any additional custom actions or methods related to the Category model here

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-updated_at')
    serializer_class = ProductRetrieveSerializer
    http_method_names = ['get', 'head', 'options']
    filterset_class = ProductFilter
    filter_backends = [SearchFilter]
    search_fields = ['translations__name'] # Add this line
    ordering_fields = ['created_at', 'name', 'type_product']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductRetrieveSerializer
        return super().get_serializer_class()

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter]
    search_fields = ['translations__name']

class ProductRatingViewSet(viewsets.ModelViewSet):
    queryset = ProductRating.objects.all().order_by(F('star').desc())
    serializer_class = ProductRatingSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()  
    serializer_class = ApplicationSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer







