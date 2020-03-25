from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View

from billplzshop.billplz.bills import create_user_bill

from .models import Product, ProductBill


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCheckoutView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        bill = create_user_bill(
            user=self.request.user,
            description=product.name,
            amount=product.price,
            redirect_url='http://staging.syafiqtermizi.com'
        )
        ProductBill.objects.create(product=product, bill=bill['bill'])
        return HttpResponseRedirect(bill['url'])
