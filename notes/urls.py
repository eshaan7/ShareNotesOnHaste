from django.urls import path

from .views import NewNote, Index, DeleteNote

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("save/", NewNote.as_view(), name="SaveNote"),
    path("delete/<int:pk>", DeleteNote.as_view(), name="DeleteNote"),
    #    path("<int:note_to_delete>/delete", views.delNote, name="delNote")
]
