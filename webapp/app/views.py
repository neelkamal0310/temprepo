from django.shortcuts import render
from .models import City

# Create your views here.


def home(request):
    cities = City.objects.all()
    return render(request, 'html/index.html', context={ 'cities': cities })
