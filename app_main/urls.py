from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('teachers/', views.teacher_page, name='teachers'),
    path('teacher/<int:id>/', views.teacher_detail, name='teacher_detail'),

    path('teachers/new', views.teacher_create, name='teacher_create'),
    path('teachers/update/<int:id>/', views.teacher_update, name='teacher_update')
]
