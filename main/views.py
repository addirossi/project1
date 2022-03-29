from django.shortcuts import render

from .models import MyModel


def products_list(request):
    products = MyModel.objects.all()
    return render(request, 'main/products_list.html', {'products': products})
