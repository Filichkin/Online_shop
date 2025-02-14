from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from cart.cart import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItem
from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    count=item['quantity']
                )
            cart.clear()
            # Запуск асинхронного залания.
            order_created.delay(order.id)
            # Задать заказ в сеансе.
            request.session['order_id'] = order.id

            return redirect('payment:process')
    else:
        form = OrderCreateForm()
    return render(
           request,
           'orders/order/create.html',
           {'cart': cart, 'form': form}
           )


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(
        request,
        'admin/orders/order/detail.html',
        {'order': order}
    )
