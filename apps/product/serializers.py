from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import Company, Product, ProductRating, CompanyProduct, Category
from rest_framework import serializers

class CategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)

    class Meta:
        model = Category
        fields = '__all__'
        ref_name = 'CategorySerializer'


class CompanySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Company)

    class Meta:
        model = Company
        fields = '__all__'
                  

class ProductSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Product)

    class Meta:
        model = Product
        fields = '__all__'



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

    
    class Meta:
        model = Product
        fields = '__all__'


