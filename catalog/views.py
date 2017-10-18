from django.shortcuts import render
from .models import Book, BookInstance, Author
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


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


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
