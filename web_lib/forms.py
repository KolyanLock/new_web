from django import forms
from django.core import validators
from django.forms import widgets
from django.core.exceptions import ValidationError

from web_lib.models import Book


class SearchAuthor(forms.Form):
    author_uuid = forms.UUIDField(label='Author UUID', required=False)


class PostAuthor(forms.Form):
    name = forms.CharField(label='Name', max_length=200, required=False)
    age = forms.IntegerField(label='Age', required=False)
    email = forms.EmailField(label='Email', required=False)


class BookForm(forms.ModelForm):
    title = forms.CharField(
        max_length=150,
        validators=[validators.RegexValidator(regex='^.{3,}$')],
        error_messages={'invalid': 'Название слишком короткое!'},
        label='Название'
    )
    color = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Book
        fields = '__all__'
        labels = {'description': 'Описание',
                  'page_num': 'Кол-во страниц',
                  'author': 'Автор',
                  'color': 'Цвет'}
        widgets = {'description': widgets.TextInput}
