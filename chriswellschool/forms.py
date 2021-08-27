from django import forms
from .models import ContactUs, RegisterStudent


class StudentRegisterForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # date_of_birth = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # current_qualification = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # course = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}))
    # profile_picture = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = RegisterStudent
        fields = ['name', 'email', 'phone', 'date_of_birth', 'current_qualification', 'course',
                  'profile_picture']


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']
