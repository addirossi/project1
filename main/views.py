from django.shortcuts import render
from .models import MyModel
from django.contrib.auth import get_user_model

def index_page(request):
    return render(request, 'index.html', {})


def products_list(request):
    products = MyModel.objects.all()
    return render(request, 'main/products_list.html', {'products': products})


def user_list(request):
    users = get_user_model().objects.all()
    return render(request, 'main/users.html', {'users': users})
