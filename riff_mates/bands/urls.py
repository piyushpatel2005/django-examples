from django.urls import path

from bands import views

urlpatterns = [
    path('musicians', views.musicians, name='musicians'),
    path('musician/<int:musician_id>', views.musician, name='musician'),
]