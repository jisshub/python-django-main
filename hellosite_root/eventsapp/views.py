from django.shortcuts import render
from .models import Event


# Create your views here.
def index(request):
    events = Event.objects.all()
    data = {'details': events}
    return render(request, 'eventsapp/index.html', data)
