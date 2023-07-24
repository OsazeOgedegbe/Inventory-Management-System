from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Item, Order, Customer
from .forms import ProductForm
import json

# Create your views here.
def home(request):
    total_product = Item.objects.count()
    total_oder = Order.objects.count()
    orders = Order.objects.all().order_by('-order_id')
    #customer = Customer.objects.get('email')
    context = {
        'product': total_product,
        'order': total_oder,
        'orders': orders
        #'customers': customer
    }
    return render(request, 'home.html', context)

def inventory(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = ProductForm()
    
    items = Item.objects.all()
    return render(request, 'inventory.html', {'items': items, 'form': form})


def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('inventory')

def increment_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.quantity += 1
    item.save()
    return redirect('inventory')

def decrement_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.quantity -= 1
    item.save()
    return redirect('inventory')

def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ProductForm(instance=item)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory')

    context = {'form': form}
    return render(request, 'edit_item.html', context)

def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

#def order_view(request):
    order_id = request.GET.get("order_id")
    order = Order.objects.get(id=order_id)
    data = {
            'order': order.order_id,
            'productname': order.product_name,
            'customermail': order.customer_mail,
            'totalprice': order.total_price,
            'shippingaddress': order.shipping_address,
            'customername': order.customer_name,
            'dateordered': order.date_ordered,
    }
    return JsonResponse(data)

#def view_order(request,pk):
    orders = get_object_or_404(Order, pk=pk)
    context = {
        'order': orders.order_id,
        'product_name': orders.product_name,
        'customer_mail': orders.customer_mail,
        'total_price': orders.total_price,
        'shipping_address': orders.shipping_address,
        'customer_name': orders.customer_name,
        'date_ordered': orders.date_ordered
    }
    return render(request, 'orders.html', context)
    #    return JsonResponse(json.dumps(context), safe=False)
#    else:
#        return JsonResponse({'error': 'Invalid request method'})

def about(request):
    return render(request, 'about.html')