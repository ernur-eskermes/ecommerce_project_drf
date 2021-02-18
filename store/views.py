from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .filters import ProductFilter
from .models import Product, Publisher, Category, Author, Genre, Contact, Review
from .serializers import (
    ProductListSerializer, ProductDetailSerializer, ProductCreateSerializer,
    AuthorListSerializer, AuthorDetailSerializer,
    PublisherSerializer,
    CategorySerializer,
    ContactListSerializer,
    GenreSerializer,
    ReviewListSerializer, ReviewDetailSerializer 
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(available=True)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'destroy':
            return ProductDetailSerializer 
        elif self.action == 'create':
            return ProductCreateSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AuthorListSerializer
        elif self.action == 'retrieve' or self.action == 'update' or \
                            self.action == 'destroy' or self.action == 'create':
            return AuthorDetailSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ReviewListSerializer
        elif self.action == 'retrieve' or self.action == 'update' or \
                            self.action == 'destroy' or self.action == 'create':
            return ReviewDetailSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
