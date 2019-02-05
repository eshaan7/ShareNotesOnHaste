from django.urls import path

from .views import Index, New_Note, Delete_Note, Edit_Note

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("add/", New_Note.as_view(), name="SaveNote"),
    path("delete/<int:pk>", Delete_Note.as_view(), name="DeleteNote"),
    path("edit/<int:pk>", Edit_Note.as_view(), name="EditNote"),
    #    path("<int:note_to_delete>/delete", views.delNote, name="delNote")
]
