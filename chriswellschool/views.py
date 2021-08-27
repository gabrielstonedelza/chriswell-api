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
