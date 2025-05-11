from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Transaction
from .forms import ProductForm, ProductTypeForm, TransactionForm
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
    return render(request, "merchstore_list.html", context)

@login_required
def merchDetail(request, pk):
    merch = get_object_or_404(Product, pk=pk)

    if merch.owner == request.user.profile:
        can_purchase = False
    else:
        can_purchase = True

    if request.method == 'POST':
        transactForm = TransactionForm(request.POST)
        if transactForm.is_valid():
            transaction = transactForm.save(commit=False)
            transaction.product = merch
            transaction.buyer = request.user.profile
            transaction.status = 'on_cart'

            merch.stock -= transaction.amount
            if merch.stock == 0:
                 merch.status = 'out_of_stock'
                 can_purchase = False
            merch.save()
            transaction.save()
        return redirect('merchstore:merchstore_cart')
    else:
            transactForm = TransactionForm(request.POST)
    context = {"merch": merch , "transact_form" : transactForm, "can_purchase":can_purchase}
    return render(request, "merchstore_detail.html", context)

@login_required
def merchCreate(request):
    if request.method == 'POST':
        productform = ProductForm(request.POST, request.FILES)
        productTypeform = ProductTypeForm(request.POST)
        if productform.is_valid():
            product = productform.save(commit=False)
            product.owner = request.user.profile
            productform.save()
        elif productTypeform.is_valid():
            productTypeform.save()
    else:
        productform = ProductForm(request.POST, request.FILES)
        productTypeform = ProductTypeForm(request.POST)

    context = {"product_form": productform, "productType_form":productTypeform}
    return render(request,'merchstore_create.html', context)

@login_required
def merchUpdate(request, pk):
    instance = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        updateform = ProductForm(request.POST, instance=instance)
        if updateform.is_valid():
            updateform.save()
            return redirect('merchstore:merchstore_list')
    else:
             updateform = ProductForm(instance=instance)
             
    context = {"update_form": updateform}
    return render(request, 'merchstore_update.html', context)

@login_required
def merchCart(request):
    transaction = Transaction.objects.filter(buyer=request.user.profile, status='on_cart').select_related('product')
    context = {"transactions": transaction}
    return render(request, "merchstore_cart.html", context)

@login_required
def merchTransactions(request):
    transaction = Transaction.objects.filter(product__owner=request.user.profile).select_related('buyer', 'product').order_by('buyer')
    context = {'transactions': transaction}
    return render(request, 'merchstore_transaction.html', context)