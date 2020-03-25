import base64
from datetime import datetime

from django.conf import settings

from .models import Billplzbill as Bill
from .exceptions import (
    Unauthorized,
    NotFound,
    UnprocessableEntity,
    TooManyRequests,
    InternalServerError,
    ServiceUnavailable
)


def response(resp):
    if resp.status_code == 401:
        raise Unauthorized
    elif resp.status_code == 404:
        raise NotFound
    elif resp.status_code == 422:
        raise UnprocessableEntity
    elif resp.status_code == 429:
        raise TooManyRequests
    elif resp.status_code == 500:
        raise InternalServerError
    elif resp.status_code == 503:
        raise ServiceUnavailable
    return { **resp.json() }


def get_auth_header():
    secret = settings.BILL_PLZ_SECRET_KEY
    secret_64 = base64.b64encode(secret.encode('ascii')).decode('ascii')
    return { 'Authorization': f'Basic {secret_64}' }


def create_bill_from_response(resp, user=None):
    bill = Bill.objects.create(
        bill_id=resp['id'],
        collection_id=resp['collection_id'],
        amount=resp['amount'],
        due_at=datetime.strptime(resp['due_at'], '%Y-%m-%d'),
        url=resp['url']
    )
    if user:
        bill.created_by = user
        bill.save()
    return bill
