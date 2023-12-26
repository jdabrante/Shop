from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.http import HttpRequest, HttpResponse

def product_list(request: HttpRequest, category_slug: str=None) -> HttpResponse:
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/products/list.html', dict(category=category, categories=categories, products=products))


def product_detail(request: HttpRequest, product_id: str, product_slug: str) -> HttpResponse:
    product = get_object_or_404(Product, id=product_id, slug=product_slug, available=True)
    return render(request, 'shop/products/detail.html', dict(product=product))

