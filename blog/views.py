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