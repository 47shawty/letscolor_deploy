from django.shortcuts import render
from store.models import Product, ReviewRating, ProductGallery
from main.models import Partners, Menu, Banners


def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')[:10]
    r_products = Product.objects.all().filter(is_available=True).order_by('-reviewrating')[:10]
    n_products = Product.objects.all().filter(is_available=True).order_by('-stock')[:6]
    partners = Partners.objects.all()
    menu = Menu.objects.all()
    banners = Banners.objects.all()
    # Get the product gallery
    product_gallery = ProductGallery.objects.all()
    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'r_products': r_products,
        'n_products': n_products,
        'reviews': reviews,
        'partners': partners,
        'menu': menu,
        'product_gallery': product_gallery,
        'banners': banners,
    }
    return render(request, 'home.html', context)
