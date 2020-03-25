from django.shortcuts import render

from django.views.generic import FormView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .forms import BillForm


class BillCallBackView(FormView):
    form_class = BillForm
    http_method_names = ['post']

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return
