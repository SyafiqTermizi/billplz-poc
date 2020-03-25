from django.contrib import admin

from .models import Billplzbill


class BillAdmin(admin.ModelAdmin):
    pass


admin.site.register(Billplzbill, BillAdmin)
