from django.shortcuts import render
# import Post and Comment models
from blog.models import Post, Comment

# Create your views here.
# inside the view function (blog_index()), we obtain a Queryset containing all the posts in the database.order_by() orders the Queryset according to the agument given, with the minus sign telling Django to start with the largest value so the posts will be ordered witht he most recent one first

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

# create blog_category() view

def blog_category(request, category):
    # below we are using a Django Queryset filter
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

    # The argument of the Django Queryset filter tells Django what conditions need to be met for an object to be retrieved.
    # In this case, we only want posts whose categories contain the category with the name corresponding to that given in the argument of the view function., and using order_by() to order posts starting with the most recent
    # Then we add these posts and the category to the context dictionary and render our template

def blog_detail(request, pk):
    # view function takes pk value as an argument and retrieves the object with the given pk
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog_detail.html", context)