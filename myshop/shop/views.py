from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Manufacture
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None, manufacture_slug=None):
    category = None
    manufacture = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    manufacturies = Manufacture.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if manufacture_slug:
        manufacture = get_object_or_404(Manufacture, slug=manufacture_slug)
        products = products.filter(manufacture=manufacture)

    query = request.GET.get("q")
    if query:
        products = Product.objects.filter(Q(name__icontains=query))

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'manufacture': manufacture,
                   'manufacturies': manufacturies,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

def pageabout(request):
    return render(request, 'pages/about.html', {})

def pagecontact(request):
    return render(request, 'pages/contact.html', {})

def pagedelivery(request):
    return render(request, 'pages/delivery.html', {})
