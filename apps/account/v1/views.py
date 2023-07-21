from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm
# from ..models import Profile
from django.conf import settings
from apps.course.models import SoldCourse


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('main:index')
    return render(request, 'account/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main:index')
    return render(request, 'account/logout.html')


class Register(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/register.html'


def profile_info(request):
    user_id = request.user.id
    profile = settings.AUTH_USER_MODEL.objects.get(user_id=user_id)
    ctx = {
        'profile': profile,
    }
    return render(request, 'account/profile_info.html', ctx)


def profile_update(request, pk):
    user = request.user
    profile = settings.AUTH_USER_MODEL.objects.get(user=user)
    if request.method == 'POST':
        email = request.POST.get('email', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        bio = request.POST.get('bio', None)
        image = request.FILES.get('image', None)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        profile.bio = bio
        if image:
            profile.image = image

        user.save()
        profile.save()
        return redirect('account:profile_info')
    ctx = {
        'profile': profile,
    }
    return render(request, 'account/profile_update.html', ctx)


def my_courses(request):
    profile_id = request.user.profile.id
    courses = SoldCourse.objects.filter(profile_id=profile_id)
    ctx = {
        'courses': courses,
    }
    return render(request, 'account/my_courses.html', ctx)

