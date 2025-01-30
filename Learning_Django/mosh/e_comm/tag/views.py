from django.shortcuts import render
from .forms import ProductForm
# Create your views here.


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = ProductForm()
    context = {
        'form': form
    }

    return render(request, 'product_create.html', context)
