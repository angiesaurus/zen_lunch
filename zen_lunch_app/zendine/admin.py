from django.contrib import admin
from zendine.models import User, UserBlacklist

admin.site.register(User)
admin.site.register(UserBlacklist)
# Register your models here.
