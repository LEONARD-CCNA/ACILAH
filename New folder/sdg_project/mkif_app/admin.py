# mkif_app/admin.py
from django.contrib import admin
from .models import ResearchDocument, InnovationProject, Communication

admin.site.register(ResearchDocument)
admin.site.register(InnovationProject)
admin.site.register(Communication)
