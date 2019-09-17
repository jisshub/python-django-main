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


def func2(request):
    states = {'each': ['kerala', 'TN', 'karnataka']}
    return render(request, 'firstApp/new.html', context=states)


def func(request):
    # payment_dict = {'id': 32328,
    #                 'payee': 'Ajith',
    #                 'amount': 3000,
    #                 }
    # data = {'name': ['ajith', 'aju', 'robin']}
    country_name = {'names': ['india', 'pakistan', 'usa']}

    return render(request, 'firstApp/dict.html', context=country_name)
