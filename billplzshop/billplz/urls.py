from django.urls import path

from .views import BillCallBackView

app_name = 'billplz'
urlpatterns = [
    path('callback', BillCallBackView.as_view(), name='callback'),
]
