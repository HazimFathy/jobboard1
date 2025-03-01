from django.shortcuts import render
from .models import contact
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def myinfo(request):
    myinfo=contact.objects.first()
    if request.method == 'POST':
        message=request.POST['message']
        email=request.POST['email']
        subject=request.POST['subject']
        print( subject)
        print( message)
        print( email)
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    return render(request,'contact/contact.html',{'myinfo':myinfo})