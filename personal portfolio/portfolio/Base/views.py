from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')

        # Validation
        if len(name) < 2 or len(name) > 30:
            messages.error(request, 'Length of name should be greater than 2 and less than 30 words.')
            return render(request, 'home.html')

        if len(email) < 5 or len(email) > 30:
            messages.error(request, 'Invalid email, please try again.')
            return render(request, 'home.html')

        if len(number) < 10 or len(number) > 12:
            messages.error(request, 'Invalid number, please try again.')
            return render(request, 'home.html')

        # Save to database
        contact = models.Contact(name=name, email=email, content=content, number=number)
        contact.save()
        messages.success(request, 'Thank You for contacting me! Your message has been saved.')

    return render(request, 'home.html')
