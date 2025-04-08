from django.shortcuts import render, redirect
from .models import Book, Author
from .forms import AuthorForm, BookForm


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_author')
    else:
        form = AuthorForm()
        
    return render(request,'book_app/add_author.html',{'form':form})
    

def add_book(request):
    if request.method=='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = BookForm()
    
    return render(request,'book_app/add_book.html',{'form':form})

def view_books(request):
    books = Book.objects.select_related('author')
    return render(request,'book_app/view_books.html',{'books':books})
            