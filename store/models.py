from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from slugify import slugify


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}-{self.id}'
            a = slugify(self.name)
            print(a)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)


class Publisher(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_list_by_publisher', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}-{self.id}'
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}-{self.id}'
        return super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')
    name = models.CharField(verbose_name='Название', max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, blank=True)
    base_photo = models.ImageField(verbose_name='Главное изображение', upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    available = models.BooleanField(verbose_name='В складе', default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор', related_name='book_author')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр', related_name='book_genre')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name='Издатель',
                                  related_name='book_publisher')

    digital = models.BooleanField(default=False)
    book_series = models.CharField(max_length=255, default='Без серии')
    age = models.CharField(max_length=255, help_text='ex. 16+', verbose_name='Возраст')
    publication_date = models.IntegerField(verbose_name='Год издания')
    size_mm = models.CharField(max_length=50, verbose_name='Размер, мм')
    binding = models.CharField(max_length=100, verbose_name='Переплет')
    weight_g = models.IntegerField(verbose_name='Вес, г')
    number_of_pages = models.IntegerField(verbose_name='Количество страниц')
    language = models.CharField(max_length=50, verbose_name='Язык')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:detail', kwargs=[self.slug])

    @property
    def get_rate(self):
        comments = self.comments.all()
        comments_rate = [comment.rate for comment in comments]
        if not comments_rate:
            return 0
        product_rate = round(sum(comments_rate) / len(comments_rate))
        return product_rate

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}-{self.id}'
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Image(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to='products/%Y/%m/%d', blank=True)
    product = models.ForeignKey(Product, verbose_name='Книга', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.id} - {self.product.name}'


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(max_length=100)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=1)
    subject = models.CharField(max_length=255, blank=True)
    text = models.TextField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
