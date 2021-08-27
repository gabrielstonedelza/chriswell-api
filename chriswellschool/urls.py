from django.urls import include, path
from . import views

urlpatterns = [
    path('student-registration/', views.register_student),
    path('contact-school/', views.contact_school),
    path('students/', views.Students.as_view())
]
