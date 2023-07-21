from django.shortcuts import render, redirect, get_object_or_404
from ..models import Course, Lesson, LessonFiles
from ...main.models import Category, Tag
from apps.main.v1.forms import SubscribeForm


def course(request):
    courses = Course.objects.order_by('-id')
    recent_course = Course.objects.order_by('-id')[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    if cat:
        courses = courses.filter(category__title__exact=cat)
    if tag:
        courses = courses.filter(tag__title__exact=tag)
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')
    ctx = {
        'recent_course': recent_course,
        'form': form,
        'categories': categories,
        'courses': courses,
        'tags': tags,
    }
    return render(request, 'course/courses.html', ctx)


def detail(request, pk):
    course_list = Course.objects.order_by('-id')
    recent_course = Course.objects.order_by('-id')[:3]
    courses = get_object_or_404(Course, id=pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    cat = request.GET.get('cat')
    if cat:
        course_list = course_list.filter(category__title__exact=cat)
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')
    ctx = {
        'recent_course': recent_course,
        'course_list': course_list,
        'form': form,
        'categories': categories,
        'tags': tags,
        'courses': courses,
    }
    return render(request, 'course/course-single.html', ctx)


def lesson_detail(request, course_id, pk):
    lesson = Lesson.objects.get(id=pk)
    randomly_5_courses = Course.objects.order_by('?')[:5]
    main_lesson = LessonFiles.objects.filter(lesson_id=pk, is_main=True).first()
    print(222222222222, main_lesson)
    ctx = {
        'lesson': lesson,
        'randomly_5_courses': randomly_5_courses,
        'main_lesson': main_lesson,
    }
    return render(request, 'course/course_lesson.html', ctx)
