from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("student-registration/", views.registration, name='registration'),
    path('contactus/', views.contact_us, name="contactus"),
    path('courses/', views.courses, name="courses"),

    # for api
    path('student-registration/', views.register_student),
    path('contact-school/', views.contact_school),
    path('students/', views.Students.as_view())
]
