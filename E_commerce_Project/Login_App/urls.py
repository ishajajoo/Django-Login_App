from . import views
from django.urls import path

urlpatterns = [
    path('Homepage/', views.HomePage),
    path('Indexpage/', views.IndexPage),
    path('all-student/', views.AllStudentDetails),
    path('student-details/<int:pk>', views.SingleStudentDetails)
]