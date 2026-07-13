from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('know-more/', views.knowmore_view, name='knowmore'),
    path('about/', views.aboutus_view, name='aboutus'),
    path('contact/', views.contact_view, name='contact'),
    path('party-hall/', views.party_view, name='party'),
    path('orders/', views.orders_view, name='orders'),
    path('room-booking/', views.roombook_view, name='roombook'),
    path('couple-room-ac/', views.couple_view, name='couple_ac'),
    path('couple-room-nonac/', views.couplenon_view, name='couple_nonac'),
    path('family-room-ac/', views.family_view, name='family_ac'),
    path('family-room-nonac/', views.familynon_view, name='family_nonac'),
    path('menu/veg/', views.veg_menu, name='veg_menu'),
    path('menu/nonveg/', views.nonveg_menu, name='nonveg_menu'),
    path('projecthotelnav/', views.projecthotelnav, name='projecthotelnav'),
    path('projecthotelnon/', views.projecthotelnon, name='projecthotelnon'),

    
    # API endpoints
    path('api/login/', views.login_api, name='login_api'),
    path('api/register/', views.register_api, name='register_api'),
    path('api/logout/', views.logout_api, name='logout_api'),
]
