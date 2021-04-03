from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail")
]

# Line 5 ( path("", views.project_index, name="project_index"), ) we hook up our app root URL to the project_index view

# Line 6 ( path("<int:pk>/", views.project_detail, name="project_detail") ) hooks up the project_detail view to our app root URL, but this one is a but more complicated
# We want the URL to be /1, /2, and so on, depending on the project's pk
# The pk value in the URL is the same pk passed to the view function, so we need to dynamically generate these URLS depending on which project the user wants to view.
# To dynamically generate URLS, wen need <int:pk> notation! It simply tells Django that the value passed in the URL is an integer, and its variable name is pk.