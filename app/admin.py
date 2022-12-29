from django.contrib import admin
from app import models

# Register your models here.

class subjectdetailsAdmin(admin.ModelAdmin):
     list_display = ['sname', 'scode','credit']
admin.site.register(models.subject, subjectdetailsAdmin)

