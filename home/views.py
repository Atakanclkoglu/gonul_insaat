from django.shortcuts import render

from home.models import *

# Create your views here.

def index(request):
    sliders = Slider.objects.all()
    about = AboutUs.objects.first()
    services=Service.objects.all()
    social_media_links = SocialMedia.objects.all()
    video = ServiceVideo.objects.first()
    projects = Project.objects.all()
    logo=Logo.objects.first()
    context = {
        'sliders': sliders,
        'about_us': about,
        'services':services,
        'social_media_links': social_media_links,
        'projects': projects,
        'logo':logo,
        'video':video
    }
    return render(request, 'index.html',context=context)
