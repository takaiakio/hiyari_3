from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('report/<int:pk>/', views.report_detail, name='report_detail'),
    path('report/<int:pk>/edit/', views.report_edit, name='report_edit'),
    path('report/<int:pk>/delete/', views.report_delete, name='report_delete'),
    path('export_csv/', views.export_csv, name='export_csv'),
    path('report/new/', views.report_create, name='report_create'),
]
