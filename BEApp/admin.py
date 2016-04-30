from django.contrib import admin
from django.contrib.auth.admin import UserAdmin	as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Car, Driver,UserProfile

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserProfileInline(admin.TabularInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Дополнительная информация'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(UserProfile)

# Register your models here.
