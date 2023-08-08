from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import Company, Product, ProductRating, CompanyProduct, Category, SubCategory
from rest_framework import serializers
from django.db.models import Avg , Sum, Count

class CategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)

    class Meta:
        model = Category
        fields = '__all__'
        ref_name = 'CategorySerializer'

class SubCategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=SubCategory)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Product)

    class Meta:
        model = Product
        fields = '__all__'
        
class CompanySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Company)
    products = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = '__all__'

    def get_products(self, instance):
        products = Product.objects.filter(campany=instance)  # Use "campany" instead of "company"
        product_serializer = ProductSerializer(products, many=True)
        return product_serializer.data


                
class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = '__all__'



class CompanyProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer()  # Capitalized field name
    product = ProductSerializer()  # Capitalized field name

    class Meta:
        model = CompanyProduct
        fields = '__all__'


class ProductRetrieveSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Product)
    
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        reviews = instance.productreview.all()
        # rewiews = ProductReview.objects.filter(product = instance) # hamma oziga boglangan review larni olish
        review_ser = ProductRetrieveSerializer(reviews, many=True)
        rep["product_reviews"] = review_ser.data
        return rep

    class Meta:
        model = Product
        fields = "__all__"

    def get_review_avg(self, obj):
        return ProductRating.objects.filter(product=obj).aggregate(Avg('star'), Sum('star'), Count('star'))