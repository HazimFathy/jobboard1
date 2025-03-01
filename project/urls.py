

from argparse import Namespace
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.conf.urls import handler500
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('dashboardsecret/', admin.site.urls  ),
    path('', lambda request: redirect('home:home')),
    path('jobs/', include('job.urls',namespace='jobs')),
    path('blogs/', include('blog.urls',namespace='blogs')),
    path('contact/', include('contact.urls',namespace='contacts')),
    path('home/', include('home.urls',namespace='home')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'accounts.views.custom_404'
handler500 = "accounts.views.custom_500"