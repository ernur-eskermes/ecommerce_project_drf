from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    Author,
    Genre,
    Publisher,
    Product,
    Category,
    Image,
    Contact,
    Review,
)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'slug')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'slug')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'slug')


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'price',
                    'author', 'genre', 'available')
    list_filter = ('available', 'created')
    list_editable = ('available',)
    search_fields = ('name', 'author__name', 'genre__name')
    inlines = [ImageInline]
    save_on_top = True
    list_display_links = ('get_image', 'name')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.base_photo.url} width="50" height="60"')

    get_image.short_description = 'Изображение'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('id', 'subject', 'status')


admin.site.site_title = 'Aroma shop api administration'
admin.site.site_header = 'Aroma shop api administration'
