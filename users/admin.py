from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from project.settings import AUTH_USER_MODEL
from .forms import UserChangeForm ,UserCreationForm
from .models import User
# Register your models here.

'''
class UserAdmin (BaseUserAdmin):
    ordering = ['email']
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    
    list_display = ['pkid','id','first_name','last_name','email','is_staff','is_active']
    list_display_links = ['email','is_staff','is_active']
    fieldsets=(
        (_("login Credentials"),{"fields":("email","password")}),
        (_("Personal Info"),{"fields":("first_name","last_name")}),
        (_("Permissions and Groups"),{"fields":("is_active","is_staff","is_superuser","groups","user_permissions")}),
        (_("Important Dates"),{"fields":("last_login","date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2"),
        }),
    )
    search_fields = ['email','first_name','last_name']
    
admin.site.register(User , UserAdmin)
'''

'''class UserAdmin (BaseUserAdmin):
    ordering = ['pkid']
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    
    list_display = ['first_name','last_name','pkid','id','is_staff','is_active','email']
    list_display_links = ['first_name','email','is_staff','is_active']
    fieldsets=(
        (_("login Credentials"),{"fields":("email","password")}),
        (_("Personal Info"),{"fields":("first_name","last_name")}),
        (_("Permissions and Groups"),{"fields":("is_active","is_staff","is_superuser","groups","user_permissions")}),
        (_("Important Dates"),{"fields":("last_login","date_joined")}),
    )
    add_fieldsets=((
        None,{
            'classes':('wide',),
            'fields':('email','first_name','last_name','password1','password2'),
        }),
    )
    
    search_fields = ['eamil','first_name','last_name']

admin.site.register(User, UserAdmin)'''


"""class UserAdmin (BaseUserAdmin):
    ordering = {'pkid'}
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    
    list_display = ['first_name','last_name','pkid','id','email','is_active','is_staff']
    list_display_links = ['email','is_staff','is_active']
    
    
    fieldsets = (
        (_('Login Credentials'), {"fields": ('email','password')}),
        (_('Personal Info'), {"fields": ('first_name','last_name')}),
        (_('Permissions and Groups'), {"fields": ('is_active','is_staff','is_superuser','user_permissions','groups')}),
        (_('Important Dates'), {"fields": ('last_login','date_joined')}),
        
    )
    
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            "fields": ('email','first_name','last_name','password1','password2'),
        }),
    )
    
    search_fields = ['first_name','last_name','email']
    
admin.site.register(User,UserAdmin)
"""


class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ['pkid']
    form = UserCreationForm
    add_form = UserChangeForm
    
    list_display = ['full_name', 'pkid' ,'id' ,'is_active','is_staff','email']
    list_display_links = ['full_name' , 'email']
    search_fields = ['first_name','last_name','email']
    
    
    fieldsets = (
        (_('Login Credentials'),{'fields':('email','password')}),
        (_('Personal Info'),{'fields':('full_name','first_name','last_name')}),
        (_('Premission and Groups'),{'fields':('is_active','is_staff','is_superuser','user_permissions','groups')}),
        (_('Important Dates'),{'fields':('last_login','date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            "fields": ('first_name','last_name','email','password1','password2'),
        }),
    )
    
admin.site.register(User,UserAdmin)