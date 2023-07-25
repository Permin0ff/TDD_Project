from django.shortcuts import render
from .forms import AddBookForm
from .models import Catalog


def home(request):
    # Save a new book to the catalogue
    if request.method == 'POST':
        add_book_form = AddBookForm(data=request.POST)
        # check if the form is valid
        if add_book_form.is_valid():
            add_book_form.save()
    # Get all books from the catalog
    books = Catalog.objects.all()
    # Show the empty form for users to fill
    add_book_form = AddBookForm()

    return render(request, 'home.html', {
        "add_book_form": add_book_form,
        "books": books
    })
