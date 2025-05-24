from ..models import AboutUs, TeamMember
from django.contrib import admin

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    fields = ('title', 'description', 'image')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'bio')
    search_fields = ('name',)
    fields = ('name', 'position', 'bio', 'image')
