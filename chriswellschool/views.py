from rest_framework import viewsets
from .models import ContactUs, RegisterStudent
from .serializers import ContactSerializer, RegisterSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .process_mail import send_my_mail
from django.conf import settings
from rest_framework.views import APIView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentRegisterForm, ContactUsForm


def csrf_failure(request, reason=""):
    return render(request, "chriswellschool/403_csrf.html")


def index(request):
    return render(request, "chriswellschool/index.html")


def registration(request):
    form = StudentRegisterForm(request.POST, request.FILES)
    if request.method == "POST":

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            current_qualification = form.cleaned_data.get('current_qualification')
            course = form.cleaned_data.get('course')
            profile_picture = form.cleaned_data.get('profile_picture')

            RegisterStudent.objects.create(name=name, email=email, phone=phone, date_of_birth=date_of_birth,
                                           current_qualification=current_qualification, course=course,
                                           profile_picture=profile_picture)
            return redirect('home')
    else:
        StudentRegisterForm()

    context = {
        "form": form
    }
    return render(request, "chriswellschool/student_registration.html", context)


def courses(request):
    return render(request, "chriswellschool/courses.html")


def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            ContactUs.objects.create(name=name, email=email, message=message)
            return redirect('home')

    else:
        form = ContactUsForm()

    context = {
        "form": form
    }

    return render(request, "chriswellschool/contactus.html", context)


@api_view(['POST'])
def contact_school(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        message = serializer.validated_data['message']
        serializer.save()
        send_my_mail(f"New message from {name}", settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER,
                     {"name": name, "message": message, "email": email},
                     "email_templates/contact_success.html")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_student(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        phone = serializer.validated_data['phone']
        serializer.save()
        send_my_mail(f"Hi from Chriswell School of Business and Technology", settings.EMAIL_HOST_USER, email,
                     {"name": name},
                     "email_templates/success.html")
        send_my_mail(f"Got new Registration", settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER,
                     {"name": name, "phone": phone, "email": email},
                     "email_templates/ownmail.html")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Students(APIView):
    def get(self, request, format=None):
        students = RegisterStudent.objects.all().order_by('-date_registered')
        serializer = RegisterSerializer(students, many=True)
        return Response(serializer.data)
