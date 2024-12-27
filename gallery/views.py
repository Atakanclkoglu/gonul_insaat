from django.shortcuts import render
from home.models import *
from gallery.models import *


def gallery(request):
    sliders = Slider.objects.all()
    about = AboutUs.objects.first()
    services=Service.objects.all()
    social_media_links = SocialMedia.objects.all()
    projects = Project.objects.all()
    gallerys = Post.objects.all()
    logo=Logo.objects.first()

    context = {
        'sliders': sliders,
        'about_us': about,
        'services':services,
        'social_media_links': social_media_links,
        'projects': projects,
        'gallerys': gallerys,
        'logo':logo
    }
    return render(request, 'gallery.html',context=context)
