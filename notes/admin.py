from django.contrib import admin
from .models import Notes
# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'note')

admin.site.register(Notes, NotesAdmin)