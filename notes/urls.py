from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:note_to_delete>/delete", views.delNote, name="delNote")
]
