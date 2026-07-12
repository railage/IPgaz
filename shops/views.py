from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.urls import reverse
from .models import Shop, Category, Product, Order

def main_page(request):
    shops = Shop.objects.all()
    return render(request, 'shops/main.html', {'shops': shops})

def shop_detail(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    categories = shop.categories.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        product_request = request.POST.get('product_request')
        if name and phone and product_request:
            Order.objects.create(
                shop=shop,
                customer_name=name,
                phone=phone,
                product_request=product_request
            )
            # Перенаправление с якорем #order
            return redirect(reverse('shop_detail', args=[shop_id]) + '?success=1#order')

    success = request.GET.get('success') == '1'
    return render(request, 'shops/shop_detail.html', {
        'shop': shop,
        'categories': categories,
        'success': 'Ваш заказ принят!' if success else None,
    })

def category_detail(request, shop_id, category_id):
    shop = get_object_or_404(Shop, id=shop_id)
    category = get_object_or_404(Category, id=category_id)
    products = category.products.filter(shops=shop)
    return render(request, 'shops/category_detail.html', {
        'category': category,
        'products': products,
        'shop_id': shop_id,
    })