from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User

User = get_user_model()

admin.site.register(User)
# Register your models here.



# class UserAdmin(admin.ModelAdmin):
#     list_display = ('first_name','last_name','email')
#     list_filter=('created_at',)
#     search_fields=('title',)

