from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
import os

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            subject = f"New Contact Form Submission from {name}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            send_mail(
                subject,
                email_message,
                os.getenv('EMAIL_HOST_USER'),  # Sender (your SMTP email)
                [os.getenv('EMAIL_HOST_USER')],  # Your email as recipient
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')

    else:
        form = ContactForm()
    
    return render(request, 'pages/contact.html', {'form': form})

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class OtherWaysToHelpView(TemplateView):
    template_name = 'pages/other_ways_to_help.html'
