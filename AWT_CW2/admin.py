from django.contrib import admin
from AWT_CW2.models import ClassModel
class ClassAdmin(admin.ModelAdmin):
    list_display = ('country', 'recovered', 'positive', 'death',)

admin.site.register(ClassModel, ClassAdmin)