from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Transaction
from django.contrib.auth.decorators import login_required


def merchList(request):
    user_profile = getattr(request.user, "profile", None)
    
    if request.user.is_authenticated:
         user_products = Product.objects.filter(owner=user_profile)
         other_products = Product.objects.exclude(owner=user_profile)

    else:
         user_products = None
         other_products = Product.objects.all()
    context = {"user_products": user_products, "other_products":other_products}
    return render(request, "merch_list.html", context)