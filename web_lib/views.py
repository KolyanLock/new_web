from django.forms import modelform_factory, widgets
from django.shortcuts import render, redirect

# Create your views here.
from web_lib.forms import SearchAuthor, PostAuthor, BookForm
from web_lib.models import Author, Book


def main(request):
    return render(request, 'web_lib/main.html', {'book_form': BookForm()})
    # return render(request, 'web_lib/main.html',
    #               {'form_book_post': modelform_factory(Book, fields='__all__',
    #                                                      labels={'title': 'Название',
    #                                                              'description': 'Описание',
    #                                                              'page_num': 'Кол-во страниц',
    #                                                              'author': 'Автор'},
    #                                                      widgets={'description': widgets.TextInput})})


# def form_search(request):
#     if request.method == 'GET':
#         return render(request, 'web_lib/main.html', {'form': SearchAuthor(request.GET)})


def authors(request):
    if 'author_uuid' in request.GET:
        return redirect('author_id', request.GET['author_uuid'])
    if request.method == 'POST':
        Author.objects.create(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            email=request.POST.get('email')
        )
    all_authors = {'authors': Author.objects.all()}
    return render(request, 'web_lib/authors.html', all_authors)


def author_id(request, pk):
    author = Author.objects.get(pk=pk)
    books_amount = author.book_set.count()
    fount_author = {'author': author, 'books_amount': books_amount}
    return render(request, 'web_lib/author_id.html', fount_author)


def books(request):
    all_books = {'books': Book.objects.all()}
    return render(request, 'web_lib/books.html', all_books)


def create_book(request):
    book_form = BookForm()
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.description = book_form.cleaned_data['description'] + ' ' + book_form.cleaned_data['color']
            book.save()
            return redirect('books')
    return render(request, 'web_lib/book_form.html', {'book_form': book_form})


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    book_form = BookForm(instance=book)
    if request.method == 'POST':
        book_form = BookForm(request.POST, instance=book)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.description = book_form.cleaned_data['description'] + ' ' + book_form.cleaned_data['color']
            book.save()
            return redirect('books')
    return render(request, 'web_lib/book_form.html', {'book_form': book_form})


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render(request, 'web_lib/delete_book.html', {'book': book})


def about(request):
    return render(request, 'web_lib/about.html')
