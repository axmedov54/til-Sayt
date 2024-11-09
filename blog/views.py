from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .models import Post, Contact, CommentPospt, Category
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# from django.views.generic import ListView

# class HomePage(ListView):
#     paginate_by = 3
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     template_name = 'index.html'



# def HomePage(request):
#     posts = Post.published.all()
#     paginator = Paginator(posts, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'index.html', {'posts':page_obj})


def ContactPage(request):
    contact = Contact()
    if request.method == "POST":
        contact.username = request.POST.get('fullName')
        contact.email = request.POST.get('email')
        contact.phone_number = request.POST.get('phone')
        contact.message = request.POST.get('message')
        contact.save()
        print("Comment saqlandi")
        return redirect('contact')    
    return render(request, 'contact.html')


def HomePage(request):
    Posts = Post.objects.all()
    return render (request,'index.html',{'posts':Posts})

def PostDatail(request, year, month, day, slug):
    usercoment = CommentPospt()
    Posts = get_object_or_404(Post, slug=slug, status="published", publish__year = year, publish__month=month, publish__day = day)
    if request.method == "POST":
        comment = request.POST.get('commentpost')
        user = request.user
        if len(comment) != 0:
            usercoment.author = user
            usercoment.post = Posts
            usercoment.comment = comment
            usercoment.save()
            return redirect('home')
    comments2 = CommentPospt.objects.filter(post=Posts).select_related('author')
    return render(request, 'post_detail.html', {'post':Posts, 'comments':comments2})


def SingupPage(request):
    if request.method == "POST":
        username = request.POST.get('name')
        useremail = request.POST.get('email')
        if request.POST.get('password1') == request.POST.get('password2'):
            password = request.POST.get('password1')
            user = User.objects.create_user(username=username, email=useremail, password=password)
            login(request, user)
            return redirect('home')
    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
            username = request.POST.get('name')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'login.html')



def LogoutUser(request):
    logout(request)
    return redirect('home')


def AboutPage(request):
    return render(request, 'about.html')


def CategoryPost(request, slug):
    object_list = Post.objects.filter(category__slug = slug)
    cat = Category.objects.filter(slug=slug)
    paginator = Paginator(object_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'posts':page_obj, 'cat':cat})