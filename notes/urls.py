from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:note_to_delete>/delete", views.delNote, name="delNote")
]
