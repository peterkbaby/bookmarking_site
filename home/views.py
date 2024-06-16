from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from .forms import BookForm
from .models import books
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'home/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],request.POST['username'], request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
                
            except IntegrityError:
                return render(request, 'home/signupuser.html', {'form': UserCreationForm, 'error': 'Username already exists'})

        else:
            return render(request, 'home/signupuser.html', {'form': UserCreationForm, 'error': 'Passwords does not match'})
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'home/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'home/loginuser.html', {'form':AuthenticationForm(), 'error':'username and password did not match'})
        else:
            login(request, user)
        return redirect('currenttodos')   
    
def home(request):
    if 'term' in request.GET:
        qs = books.objects.filter(title__startswith=request.GET.get('term'))
        titles = list()
        for booksa in qs:
            titles.append(booksa.title)
        return JsonResponse(titles, safe=False)
    return render(request, 'home/home.html')
           

@login_required       
def currenttodos(request):
    bookss = books.objects.filter(user = request.user).order_by('-created')
    paginator = Paginator(bookss, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/current.html', {'bookss':bookss, 'page_obj': page_obj})
@login_required
def createbook(request):
    if request.method == 'GET':
        return render(request, 'home/create.html', {'form': BookForm()})
    else:
        if books.objects.filter(user=request.user).count() >= 5:
            return render(request,'home/create.html',{'form': BookForm(), 'error': 'You can only add up to 5 bookmarks'})
        try:
            form = BookForm(request.POST)
            newbook = form.save(commit=False)
            newbook.user = request.user
            newbook.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'home/create.html', {'form': BookForm(), 'error': 'bad data passed in'})
@login_required
def viewbook(request, book_pk):

    bookss = get_object_or_404(books, pk=book_pk, user=request.user)
    if request.method == 'GET':
        form = BookForm(instance=bookss)
        return render(request, 'home/viewbook.html', {'bookss': bookss, 'form': form})
    else:
        try:
            form = BookForm(request.POST, instance=bookss)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'home/viewbook.html', {'bookss': bookss, 'form': form, 'error': 'Bad Information passed in'})
@login_required       
def deletebook(request, book_pk):
    bookss = get_object_or_404(books, pk=book_pk, user=request.user)
    if request.method == 'POST':
        bookss.delete()
        return redirect('currenttodos')
    
#def autocomplete(request):
    
    

