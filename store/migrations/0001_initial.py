# Generated by Django 3.1.6 on 2021-02-12 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Издатель',
                'verbose_name_plural': 'Издатели',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255)),
                ('base_photo', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Главное изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('available', models.BooleanField(default=False, verbose_name='В складе')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('digital', models.BooleanField(default=False)),
                ('book_series', models.CharField(default='Без серии', max_length=255)),
                ('age', models.CharField(help_text='ex. 16+', max_length=255, verbose_name='Возраст')),
                ('publication_date', models.IntegerField(verbose_name='Год издания')),
                ('size_mm', models.CharField(max_length=50, verbose_name='Размер, мм')),
                ('binding', models.CharField(max_length=100, verbose_name='Переплет')),
                ('weight_g', models.IntegerField(verbose_name='Вес, г')),
                ('number_of_pages', models.IntegerField(verbose_name='Количество страниц')),
                ('language', models.CharField(max_length=50, verbose_name='Язык')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='store.author', verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category', verbose_name='Категория')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_genre', to='store.genre', verbose_name='Жанр')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_publisher', to='store.publisher', verbose_name='Издатель')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_list', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.product', verbose_name='Книга')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField(default=1)),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('comment', models.TextField(blank=True, max_length=500)),
                ('status', models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
