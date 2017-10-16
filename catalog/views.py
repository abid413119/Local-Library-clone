from django.shortcuts import render
from .models import Book, BookInstance, Author
from django.views.generic import ListView, DetailView


def index(request):
    """
    view function for homepage
    :param request:
    :return:
    """
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()

    available_books = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()

    context = {
        'num_books': num_books,
        'num_instances': num_instance,
        'available_books': available_books,
        'num_authors': num_authors,
    }

    return render(request, 'catalog/index.html', context=context)


class BookListView(ListView):
    model = Book
    paginate_by = 10


class BookDetailView(DetailView):
    model = Book


class AuthorList(ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(DetailView):
    model = Author
