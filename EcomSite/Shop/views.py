from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.
def Index(request):
    Product_object = Product.objects.all()

    ItemName = request.GET.get('ItemName')

    #Search code
    if ItemName != '' and ItemName is not None:
        Product_object = Product_object.filter(Title__icontains = ItemName)

    #Paginator code
    paginator = Paginator(Product_object,4)
    page = request.GET.get('page')
    Product_object = paginator.get_page(page)

    return render(request,'Shop/Index.html',{'Product_object': Product_object})


def Detail(request,id):
    Product_object = Product.objects.get(id=id)
    return render(request,'Shop/detail.html',{'Product_object':Product_object})