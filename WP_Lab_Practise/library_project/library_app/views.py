from django.shortcuts import render, redirect
from .models import Book, Borrower, Issue
from .forms import BookForm, BorrowForm, IssueForm



def dashboard(reqeust):
    issues = Issue.objects.all()
    return render(reqeust,'library_app/dashboard.html',{'issues':issues})
    

    
def add_borrower(request):
    if request.method=='POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BorrowForm()
    
    return render(request,'library_app/add_borrower.html',{'form':form})

def add_book(request):
    if request.method=='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BookForm()
    
    return render(request,'library_app/add_book.html',{'form':form})

def issue_book(request):
    if request.method=='POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue=form.save()
            issue.book.is_available=False
            issue.book.save()
            return redirect('dashboard')
    else:
        form = IssueForm()
    return render(request,'library_app/issue_book.html',{'form':form})
     
