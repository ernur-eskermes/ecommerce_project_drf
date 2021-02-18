from rest_framework import serializers

from .models import Product, Publisher, Category, Author, Review, Contact, Genre, Image


class ReviewListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'rate', 'user')


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image',)


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name',)


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    author = AuthorListSerializer()
    genre = serializers.SlugRelatedField(slug_field='name', read_only=True)
    publisher = serializers.SlugRelatedField(slug_field='name', read_only=True)
    reviews = ReviewListSerializer(many=True)
    images = ImageListSerializer(many=True)

    class Meta:
        model = Product
        exclude = ('available',)


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
