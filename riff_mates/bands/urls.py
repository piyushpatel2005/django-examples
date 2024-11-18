from django.urls import path

from bands import views

urlpatterns = [
    path('musicians', views.musicians, name='musicians'),
    path('musician/<int:musician_id>', views.musician, name='musician'),
    path("band/<int:band_id>/", views.band, name="band"),
    path("bands/", views.bands, name="bands"),
    path("venues/", views.venues, name="venues"),
]