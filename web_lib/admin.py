from django.contrib import admin

# Register your models here.
from django.shortcuts import redirect
from django.urls import path
from django.utils.html import format_html

from web_lib.models import Author, Book, Review, Product, Store


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email', 'info']
    change_list_template = 'web_lib/button.html'
    change_form_template = 'web_lib/custom_change_form.html'

    def get_urls(self):
        my_url = [path('button', self.button)]
        return super().get_urls() + my_url

    def button(self, req):
        return redirect('..')

    def info(self, obj):
        return format_html('<br>'.join(obj.info()))
    info.short_description = 'Информация'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['books'] = Author.objects.get(pk=object_id).book_set.all()
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'page_num']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', 'published']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Store)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name']
