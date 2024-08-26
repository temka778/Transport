from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
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

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.technique = Technique.objects.get(pk=self.kwargs['technique_id'])
        rental_duration = (form.instance.end_date - form.instance.start_date).days
        form.instance.total_cost = rental_duration * form.instance.technique.daily_rate
        return super().form_valid(form)
