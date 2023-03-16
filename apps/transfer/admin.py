from django.contrib import admin

from .models import HistoryTransfer

# Register your models here.
class HistoryTransferAdmin(admin.ModelAdmin):
    list_display = ('from_user','to_user', 'is_completed','created_at','amount', )
    list_filter = ('from_user','to_user', 'is_completed','created_at','amount', )
    search_filter = ('from_user','to_user', 'is_completed','created_at','amount', )
    list_per_page = 5

admin.site.register(HistoryTransfer,HistoryTransferAdmin)