from django.urls import path

from web_lib.views import main, authors, books, about, author_id

urlpatterns = [
    path('', main, name='web_lib'),
    path('authors', authors, name='authors'),
    path('author/<uuid:pk>', author_id, name='author_id'),
    path('books', books, name='books'),
    path('about', about, name='about'),
]
