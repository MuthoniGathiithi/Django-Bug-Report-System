from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('bug/<int:pk>/', views.bug_detail, name='bug_detail'),
    path('submit/', views.submit_bug, name='submit_bug'),
    path('bug/<int:pk>/update/', views.update_bug, name='update_bug'),
    path('request-admin/', views.request_admin_role, name='request_admin_role'),
    path('profile/', views.profile, name='profile'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
] 