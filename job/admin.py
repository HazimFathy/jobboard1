from django.contrib import admin
from .models import Job , category , apply
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ['title','id','owner','category',]
    list_display_links = ['title',]
    search_fields = ('title', 'description')  # 🔍 إضافة البحث في العنوان والوصف

admin.site.register(Job , JobAdmin)
admin.site.register(category)
admin.site.register(apply)