from django.contrib import admin
from .models import User
from .models import SMS_auth

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

class SMSAuthAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(SMS_auth, SMSAuthAdmin)