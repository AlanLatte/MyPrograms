from django.shortcuts import render


def index(request):
    return render(request, 'index/deadline.html')
# Create your views here.
