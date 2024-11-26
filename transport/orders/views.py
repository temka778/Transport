from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from services.models import Technique
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm


@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.delete()
    return redirect('profile')


@login_required
def ajax_order_form(request, technique_id):
    """Возвращаем форму для заказа в модальном окне"""
    technique = Technique.objects.get(pk=technique_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.technique = technique
            rental_duration = (order.end_date - order.start_date).days + 1
            order.total_cost = rental_duration * technique.daily_rate
            order.save()
            send_mail(
                'Новый заказ!',
                (
                    f'Поступил новый заказ!\n'
                    f'Номер телефона заказчика: {order.user.phone_number};\n'
                    f'Электронная почта заказчика: {order.user.email};\n'
                    f'Техника: {technique.name};\n'
                    f'Требования заказчика: {order.additional_requirements};\n'
                    f'Начало аренды: {order.start_date};\n'
                    f'Окончание аренды: {order.end_date};\n'
                    f'Общая стоимость: {order.total_cost} руб.'
                ),
                None,
                ['nnk@ннк-сервис.рф'],  # Почта компании
            )
            return JsonResponse({'message': 'Заказ успешно оформлен!'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = OrderForm()
        return render(request, 'orders/order_form.html', {'form': form, 'technique': technique})


def technique_detail_view(request, technique_id):
    technique = Technique.objects.get(pk=technique_id)
    open_modal_after_auth = request.GET.get('open_modal', False)
    return render(request, 'services/technique_detail.html', {
        'technique': technique,
        'open_modal_after_auth': open_modal_after_auth
    })