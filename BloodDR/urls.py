from django.urls import path
from . import views
urlpatterns = [
    path("", views.ShowData, name='BloodG'),
    path("index/", views.index, name='Insert_data'),
    path("savedata/", views.InsertData, name='savedata')
]