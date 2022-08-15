from django.urls import path

from web_lib.views import main, authors, books, about, author_id, create_book, update_book, delete_book

urlpatterns = [
    path('', main, name='web_lib'),
    path('authors', authors, name='authors'),
    path('author/<uuid:pk>', author_id, name='author_id'),
    path('books', books, name='books'),
    path('about', about, name='about'),
    path('create-book', create_book, name='create_book'),
    path('update-book/<int:pk>', update_book, name='update_book'),
    path('delete-book/<int:pk>', delete_book, name='delete_book'),
]
