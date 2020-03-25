from django.apps import AppConfig
from django.conf import settings

from django.urls import reverse


class BillplzConfig(AppConfig):
    name = 'billplzshop.billplz'

    def ready(self):
        try:
            settings.BILL_PLZ_SECRET_KEY
            settings.BILL_PLZ_XSIG
            settings.BILL_PLZ_COLLECTION
        except AttributeError:
            raise AttributeError('Plz set BILL_PLZ keys')

        try:
            settings.BILL_PLZ_CALLBACK_URL
        except AttributeError:
            setattr(settings, 'BILL_PLZ_CALLBACK_URL', '/billplz/cb')
