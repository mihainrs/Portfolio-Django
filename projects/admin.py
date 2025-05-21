from django.contrib import admin
from .models import Project, AboutMe, PlaygroundProjects

# Register your models here.

admin.site.register(Project)
admin.site.register(AboutMe)
admin.site.register(PlaygroundProjects)