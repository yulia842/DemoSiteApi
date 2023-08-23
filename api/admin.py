from django.contrib import admin
from .models import Skill, Project, ProjectRating, Education

# Register your models here.

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ProjectRating)
admin.site.register(Education)