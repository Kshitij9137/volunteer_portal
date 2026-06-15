from django.urls import path
from . import views

urlpatterns = [
    path('',                          views.dashboard,          name='dashboard'),
    path('accounts/signup/',          views.signup_view,        name='signup'),
    path('volunteers/',               views.volunteer_list,     name='volunteer_list'),
    path('volunteers/add/',           views.volunteer_add,      name='volunteer_add'),
    path('volunteers/export/',            views.export_csv,         name='export_csv'),
    path('volunteers/<int:pk>/edit/', views.volunteer_edit,     name='volunteer_edit'),
    path('volunteers/<int:pk>/delete/', views.volunteer_delete, name='volunteer_delete'),
    path('volunteers/<int:pk>/',      views.volunteer_detail,   name='volunteer_detail'),
]