from django.shortcuts import render, get_object_or_404, redirect, reverse
from apps.main.models import Category, Tag
from apps.blog.models import Post, Comment, Body
from apps.course.models import Course
from apps.main.v1.forms import SubscribeForm
from .forms import CommentForm


def blog(request):
    posts = Post.objects.order_by('-id')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent_courses = Course.objects.order_by('id')[::2]
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    if tag:
        posts = posts.filter(tag__title__exact=tag)
    if cat:
        posts = posts.filter(category__title__exact=cat)
    ctx = {
        'recent_courses': recent_courses,
        'posts': posts,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'blog/blog.html', ctx)


def detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    post_tag = get_object_or_404(Tag, id=pk)
    body = get_object_or_404(Body, id=pk)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    recent_courses = Course.objects.order_by('id')[::2]
    comments = Comment.objects.filter(post_id=pk, parent_comment__isnull=True)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if not request.user.is_authenticated:
            return redirect('account:login')
        if comment_form.is_valid():
            # obj = comment_form.save(commit=False)
            # obj.author_id = request.user.id
            # obj.post_id = request.pk
            # obj.parent_comment_id = request.comment_id
            # obj.body = request.body
            # obj.save()
            comment_id = request.GET.get('comment_id', None)
            body = request.POST.get('body')
            author_id = request.user.id
            if body:
                obj = Comment(comment_id=comment_id, post_id=pk, author_id=author_id)
                obj.save()
            return redirect(reverse('blog:detail', kwargs={"pk": pk}))
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')
    ctx = {
        'comment_form': comment_form,
        'comments': comments,
        'post_tag': post_tag,
        'form': form,
        'body': body,
        'tags': tags,
        'post': post,
        'categories': categories,
        'recent_courses': recent_courses,
    }
    return render(request, 'blog/blog-single.html', ctx)
