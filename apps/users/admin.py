from django.contrib import admin

from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','wallet_address', 'email','phone_number','age', 'balance')
    list_filter = ('username','wallet_address', 'email','phone_number','age', 'balance')
    search_filter = ('username','wallet_address', 'email','phone_number','age', 'balance')
    list_per_page = 5


admin.site.register(User,UserAdmin)



