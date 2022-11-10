from django.contrib import admin

from commercial_network.models import CommercialNetwork




# Register your models here.

@admin.register(CommercialNetwork)
class CommercialNetworkAdmin(admin.ModelAdmin):
    list_display = ['companies_chain']
