from django.shortcuts import render, redirect

from django.conf import settings
from .forms import ContactForm, SubscribeForm
from apps.main.models import Contact, FAQ, Answer, Category, Tag

from apps.course.models import Course, Lesson
# from ...account.models import Profile
from ...blog.models import Post


def navbar(request):
    categories = Category.objects.order_by('-id')
    courses = Course.objects.order_by('-id')
    cat = request.GET.get('cat')
    search = request.GET.get('search')
    if search:
        courses = courses.filter('search')
    if cat:
        courses = courses.filter(category__title__exact=cat)
    ctx = {
        'categories': categories,
        'courses': courses,
    }
    return render(request, 'nav.html', ctx)


def footer(request):
    last_3_blog = Post.objects.order_by('-id')[:3]
    ctx = {
        'last_3_blog': last_3_blog,
    }
    return render(request, 'footer.html', ctx)


def index(request):
    courses = Course.objects.order_by('-id')
    categories = Category.objects.all()
    users = settings.AUTH_USER_MODEL.objects.all()
    recent_blog = Post.objects.order_by('-id')[1]
    blogs = Post.objects.all()
    cat = request.GET.get('cat')
    if cat:
        courses = courses.filter(category__title__exact=cat)
    ctx = {
        'recent_blog': recent_blog,
        'blogs': blogs,
        'users': users,
        'courses': courses,
        'categories': categories,
    }
    return render(request, 'main/index.html', ctx)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')
    sub_form = SubscribeForm()
    if request.method == 'POST':
        sub_form = SubscribeForm(data=request.POST)
        if sub_form.is_valid():
            sub_form.save()
            return redirect('.')
    ctx = {
        'form': form,
        'sub_form': sub_form,
    }
    return render(request, 'main/contact.html', ctx)


def about(request):
    # faq = FAQ.objects.all()
    answer = Answer.objects.all()
    sub_form = SubscribeForm()
    if request.method == 'POST':
        sub_form = SubscribeForm(data=request.POST)
        if sub_form.is_valid():
            sub_form.save()
            return redirect('.')
    ctx = {
        'sub_form': sub_form,
        'answer': answer,
    }
    return render(request, 'main/about.html', ctx)





