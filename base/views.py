from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from base.models import *


def index(request):
    user = User.objects.get(email='azeezadedeji638@gmail.com')
    practice = practicearea.objects.all()
    purpose = ourpurpose.objects.all()
    quest = question.objects.all()

    context = {'user': user, 'practice': practice, 'purpose': purpose, 'question': quest}
    return render(request, 'base/index.html', context)


def contact(request):
    user = User.objects.get(email='azeezadedeji638@gmail.com')
    practice = practicearea.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
      # subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        try:
            send_mail(subject=name, message=message + "\n" + "This is my email address: " + email,
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=['speedoo24434@gmail.com'])
            messages.success(request, 'Your message was sent successfully, we will get back to you very soon')
        except:
            messages.error(request, 'Error occur please make sure you have internet access')

    context = {'user': user, 'practice': practice}
    return render(request, 'base/contact.html', context)


def about(request):
    user = User.objects.get(email='azeezadedeji638@gmail.com')
    practice = practicearea.objects.all()
    context = {'user': user, 'practice': practice}
    return render(request, 'base/about.html', context)

# def post(requst):
#     return render(requst, 'base/post.html')
