from django.shortcuts import render

# Create your views here.

# Below we defined a VIEW FUNCTION called hello_world()
# When the view fn is called, it will render an HTML file called hello_world.html
# View fn takes one argument: request
# This object is an HttpRequestObject that is created every time a page is loaded
# HttpRequestObject contains info about the request,like the method that can take several values including GET and POST

def hello_world(request):
    # render() looks for HTML templates inside a directory called templates insode your app directory.
    return render(request, 'hello_world.html', {})