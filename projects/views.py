from django.shortcuts import render

# import Project class from models.py
from projects.models import Project

# Create your views here.
# create a function project_index() that renders a project_index.html template

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

# Line 10 (projects = Project.objects.all() performs a query)
# a query is a command that allows you to CRUD (create, retrieve, update, delete) objects (or rows) in your database. In this case, we are retrieving all objects in the projects table

# A database query returns a collection of all objects that match the query, AKA Queryset. In this case, we want all objects in the table, so itwill return a collection of all projects

# Line 11 (context = {) we define the dictionary context
# The dictionary only has one entry (projects) to which we assign our Queryset containing all projects
# The context dictionary is used to send info to our template. Every vew function you create needs to have a context dictionary.

# Line 14 (return render (request, 'project_index.html', context)) adds context as an argument to render()
# Any entries in the context dictionary are available in the template as long as the context argument is passed to render()
# You MUST create a context dictionary and pass it to render in each view function you create

# Create project_detail() view function, which needs an additional argument, the ID of the project being viewed
def project_detail