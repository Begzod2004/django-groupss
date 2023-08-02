
from requests import Response
from rest_framework import viewsets
from .serializers import CompanySerializer, ProductSerializer, ProductRatingSerializer, ProductRetrieveSerializer
from .models import Company, Product, ProductRating
from .filters import ProductFilter


from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'head', 'options']
    lookup_field = 'slug'

    # Add any additional custom actions or methods related to the Category model here

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-updated_at')
    serializer_class = ProductSerializer
    http_method_names = ['get', 'head', 'options']
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductRetrieveSerializer
        return super().get_serializer_class()
    
    def retrieve(self, request, *args, **kwargs):
        saved_views = request.session.get('views', [])
        Product = self.get_object()
        if Product.id not in saved_views:
            Product.views += 1
            Product.save()
            saved_views.append(Product.id)
            request.session['views'] = saved_views
        return super().retrieve(request, *args, **kwargs)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ProductRatingViewSet(viewsets.ModelViewSet):
    queryset = ProductRating.objects.all()
    serializer_class = ProductRatingSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

