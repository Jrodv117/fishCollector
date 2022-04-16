from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fishes/', views.fishes_index, name='index'),
    path('fishes/<int:fish_id>/', views.fishes_detail, name='detail'),
    path('fishes/create/', views.FishCreate.as_view(), name='fishes_create'),
    path('fishes/<int:pk>/update/', views.FishUpdate.as_view(), name='fishes_update'),
    path('fishes/<int:pk>/delete/', views.FishDelete.as_view(), name='fishes_delete'),
    path('fishes/<int:fish_id>/add_bait/', views.add_bait, name='add_bait'),
    path('locations/', views.LocationList.as_view(), name='locations_index'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(), name='locations_detail'),
    path('locations/create/', views.LocationCreate.as_view(), name="locations_create"),
    path('locations/<int:pk>/update/', views.LocationUpdate.as_view(), name='locations_update'),
    path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='locations_delete'),
    path('fishes/<int:fish_id>/assoc_location/<int:location_id>/', views.assoc_location, name="assoc_location")
]
