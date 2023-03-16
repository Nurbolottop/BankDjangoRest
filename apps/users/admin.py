from django.contrib import admin

from .models import User,HistoryTransfer

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','wallet_address', 'email','phone_number','age', 'balance')
    list_filter = ('username','wallet_address', 'email','phone_number','age', 'balance')
    search_filter = ('username','wallet_address', 'email','phone_number','age', 'balance')
    list_per_page = 5

class HistoryTransferAdmin(admin.ModelAdmin):
    list_display = ('from_user','to_user', 'is_completed','created_at','amount', )
    list_filter = ('from_user','to_user', 'is_completed','created_at','amount', )
    search_filter = ('from_user','to_user', 'is_completed','created_at','amount', )
    list_per_page = 5
    
admin.site.register(User,UserAdmin)
admin.site.register(HistoryTransfer,HistoryTransferAdmin)


