from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__name')
    genre = filters.CharFilter(field_name='genre__name')
    publisher = filters.CharFilter(field_name='publisher__name')
    price = filters.RangeFilter()

    class Meta:
        model = Product
        fields = ('category', 'genre', 'publisher', 'price')
