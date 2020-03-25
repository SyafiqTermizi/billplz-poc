import hmac
import hashlib
from datetime import datetime

from django import forms
from django.conf import settings

from .models import Billplzbill as Bill


class BillForm(forms.Form):
    id = forms.CharField(max_length=255, strip=True)
    collection_id = forms.CharField(max_length=255, strip=True)
    paid = forms.CharField(max_length=255, strip=True)
    state = forms.CharField(max_length=255, strip=True)
    amount = forms.CharField(max_length=255, strip=True)
    paid_amount = forms.CharField(max_length=255, strip=True)
    due_at = forms.CharField(max_length=255, strip=True)
    email = forms.CharField(max_length=255, strip=True)
    mobile = forms.CharField(max_length=255, strip=True, required=False)
    name = forms.CharField(max_length=255, strip=True)
    url = forms.CharField(max_length=255, strip=True)
    paid_at = forms.CharField(max_length=255, strip=True)
    x_signature = forms.CharField(max_length=255, strip=True)

    def clean(self):
        cleaned_data = super().clean()
        x_signature = cleaned_data.pop('x_signature')

        form_values = []
        for key, value in cleaned_data.items():
            form_values.append(f'{key}{value}')
        form_values.sort()

        piped_form_values = ''
        for item in form_values:
            piped_form_values += (item + '|')

        piped_form_values = piped_form_values.strip('|')
        piped_form_values = bytes(piped_form_values, 'ascii')

        secret = bytes(settings.BILL_PLZ_XSIG, 'ascii')

        sig = hmac\
                .new(secret, piped_form_values, digestmod=hashlib.sha256)\
                .hexdigest()
        if sig != x_signature:
            raise forms.ValidationError('Value mismatch')

    def save(self):
        data = self.cleaned_data
        try:
            bill = Bill.objects.get(bill_id=data['id'])
        except Bill.DoesNotExist:
            pass
        else:
            bill.paid = True if data['paid'] == 'true' else False
            bill.state = data['state']
            bill.paid_amount = data['paid_amount']
            bill.paid_at = datetime.strptime(
                data['paid_at'],
                '%Y-%m-%d %H:%M:%S %z'
            )
            bill.save()