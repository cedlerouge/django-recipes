from django.contrib import admin


from django.contrib.auth.admin import UserAdmin
from recipes.apps.accounts.models import CustomUser

#admin.site.register(CustomUser)
#class CustomUserAdmin(admin.ModelAdmin):
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('email', 'last_name', 'first_name')

#admin.site.register(CustomUser, UserAdmin)
admin.site.register(CustomUser, CustomUserAdmin)