from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# def index(request):
#     html = """<h2>Django</h2>
#               <p style="color: blue";>Welcome to Django FrameWork</p>
#             """
#     return HttpResponse(html)
#

def app(request):
    pass
    return render(request, 'firstApp/home.html')


def about(request):
    pass
    return render(request, 'firstApp/about.html')


def home(request):
    # print('hai')
    return render(request, 'firstApp/index.html')
