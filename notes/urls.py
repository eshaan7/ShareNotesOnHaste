from django.urls import path

from .views import NewNote, Index, DeleteNote, EditNote

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("add/", NewNote.as_view(), name="SaveNote"),
    path("delete/<int:pk>", DeleteNote.as_view(), name="DeleteNote"),
    path("edit/<int:pk>", EditNote.as_view(), name="EditNote"),
    #    path("<int:note_to_delete>/delete", views.delNote, name="delNote")
]
