from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from .models import Order
from .forms import OrderForm
from services.models import Technique
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'
    success_url = reverse_lazy('profile')


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