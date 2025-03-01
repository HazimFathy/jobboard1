from django.urls import path , include
from . import views

app_name='accounts'

urlpatterns = [
    # signup url
    path('signup',views.signup,name='signup' ),
    # profile url
    path('profile/',views.profile_view,name='profile' ),
    # edit profile url
    path('profile/edit',views.profile_edit,name='profile_edit' ),
]
