
from .models import blogmod

from .forms import UserForm,BlogForm
from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout

from django.db.models import Q



def index(request):
    if not request.user.is_authenticated():
        return render(request, 'blog/login.html')
    else:
        all_blog = blogmod.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            albums = all_blog.filter(
                Q(album_title__icontains=query) |
                Q(artist__icontains=query)
            ).distinct()
            return render(request, 'blog/index.html', {'all_blog': all_blog})
        else:
            return render(request, 'blog/index.html', {'all_blog': all_blog})



def create_blog(request):
    if not request.user.is_authenticated():
        return render(request, 'blog/login.html')
    else:
        form = BlogForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            all_blog = form.save(commit=False)
            all_blog.user = request.user
            all_blog.save()
            return redirect('blog:index')
        context = {
            "form": form,
        }
        return render(request, 'blog/blogmod_form.html', context)

def UserRegister(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_blog = blogmod.objects.filter(user=request.user)
                return render(request, 'blog/index.html', {'all_blog': all_blog})
    context = {
        "form": form,
    }
    return render(request, 'blog/registration_form.html', context)



def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'blog/login.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_blog = blogmod.objects.filter(user=request.user)
                return render(request, 'blog/index.html', {'all_blog': all_blog})
            else:
                return render(request, 'blog/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'blog/login.html', {'error_message': 'Invalid login'})
    return render(request, 'blog/login.html')


