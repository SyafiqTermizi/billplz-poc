import requests

from django.conf import settings
from django.contrib.auth import get_user_model

from .utils import response, get_auth_header, create_bill_from_response
from .models import Billplzbill as Bill
from .models import BillPlzUser

BASE_URL = 'https://www.billplz-sandbox.com/api/'
UserModel = get_user_model()


def create_user_bill(user, description, amount, redirect_url=''):
    """
    create a bill for a django user and redirect to bill URL
    """
    data = {
        'collection_id': settings.BILL_PLZ_COLLECTION,
        'email': user.email,
        'name': user.username,
        'amount': amount,
        'callback_url': settings.BILL_PLZ_CALLBACK_URL,
        'description': description,
    }

    if redirect_url:
        data['redirect_url'] = redirect_url

    resp = response(requests.post(
        url=f'{BASE_URL}v3/bills',
        headers=get_auth_header(),
        data=data
    ))
    bill = create_bill_from_response(resp, user)
    return { 'bill': bill, 'url': resp['url'] }


def create_bill(email, name, amount, description, redirect_url=''):
    """
    create a bill and redirect to bill URL
    """
    data = {
        'collection_id': settings.BILL_PLZ_COLLECTION,
        'email': email,
        'name': name,
        'amount': amount,
        'callback_url': settings.BILL_PLZ_CALLBACK_URL,
        'description': description,
    }

    if redirect_url:
        data['redirect_url'] = redirect_url

    resp = response(requests.post(
        url=f'{BASE_URL}v3/bills',
        headers=get_auth_header(),
        data=data
    ))

    bill = create_bill_from_response(resp)
    bill_user = BillPlzUser.objects.create(
        name=resp['name'],
        email=resp['email'],
        bill=bill
    )
    return { 'bill': bill, 'url': resp['url'] }
