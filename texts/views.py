from django.shortcuts import render
from .models import HomeSlide, Announcement, Testimonial, Doctor, ContactInfo, AboutPage

def home(request):
    context = {
        'slides': HomeSlide.objects.filter(is_active=True).order_by('order'),
        'announcements': Announcement.objects.filter(is_active=True).order_by('-created_at'),
        'testimonials': Testimonial.objects.filter(is_active=True).order_by('order')[:3],
        'doctors': Doctor.objects.filter(is_active=True).order_by('order'),
        'contact': ContactInfo.objects.first(),
    }
    return render(request, 'home.html', context)

def about(request):
    about = AboutPage.objects.first()  # Get the singleton instance
    context = {
        'about': about,  # This makes {{ about }} available in the template
    }
    return render(request, 'about.html', context)

