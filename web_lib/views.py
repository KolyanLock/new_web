from django.shortcuts import render, redirect

# Create your views here.
from web_lib.forms import SearchAuthor, PostAuthor
from web_lib.models import Author, Book


def main(request):
    return render(request, 'web_lib/main.html', {'form_search': SearchAuthor(request.GET),
                                                 'form_post': PostAuthor(request.POST)})
    # return render(request, 'web_lib/main.html')


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


def about(request):
    return render(request, 'web_lib/about.html')
