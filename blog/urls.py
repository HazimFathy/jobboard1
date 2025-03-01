from django.urls import path , include
from . import views


app_name='blogs'

urlpatterns = [
    path('',views.bloglist.as_view(),name='blog' ),
    path('<int:id>',views.blog_detail,name='blogdetail'),
    path('add_blog',views.add_blog,name='addblog'),
]