from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('billplzshop.products.urls')),
    path('billplz/', include('billplzshop.billplz.urls'))
]
