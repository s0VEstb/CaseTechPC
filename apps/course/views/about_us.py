from ..models.about_us import AboutUs, TeamMember
from django.core.paginator import Paginator
from django.shortcuts import render


def about_us(request):
    """
    Рендерит страницу «О нас» с описаниями и членами команды.
    """
    about_sections = AboutUs.objects.all()
    team_members   = TeamMember.objects.all()
    return render(request, 'about_us.html', {
        'about_sections': about_sections,
        'team_members':   team_members,
    })


def home_view(request):
    return render(request, "home.html")