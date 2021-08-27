from django.db import models
from django.utils.text import slugify
from PIL import Image

COURSES = (
    ("DIPLOMA IN ACCOUNTING", "DIPLOMA IN ACCOUNTING"),
    ("DIPLOMA IN BUSINESS ADMINISTRATION", "DIPLOMA IN BUSINESS ADMINISTRATION"),
    ("DIPLOMA IN OFFICE MANAGEMENT ", "DIPLOMA IN OFFICE MANAGEMENT "),
    ("DIPLOMA IN INFORMATION TECHNOLOGY ", "DIPLOMA IN INFORMATION TECHNOLOGY "),
    ("CERTIFICATE IN ACCOUNTING ", "CERTIFICATE IN ACCOUNTING"),
    ("CERTIFICATE IN BUSINESS STUDIES ", "CERTIFICATE IN BUSINESS STUDIES"),
    ("CERTIFICATE IN SECRETARIAL DUTIES ", "CERTIFICATE IN SECRETARIAL DUTIES "),
    ("WEB DEVELOPMENT", "WEB DEVELOPMENT"),
    ("MOBILE APP DEVELOPMENT", "MOBILE APP DEVELOPMENT"),
    ("NETWORKING", "NETWORKING"),
)


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} just sent a message"


class RegisterStudent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True, help_text="Please make sure this is a working email")
    phone = models.CharField(max_length=20, help_text="We will be reaching on this line")
    date_of_birth = models.CharField(max_length=20, help_text="Format = YY-MM-DD", blank=True)
    current_qualification = models.CharField(max_length=200, blank=True)
    course = models.CharField(max_length=300)
    profile_picture = models.ImageField(upload_to="student_pics", blank=True)
    approved = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, default='', blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_post_url(self):
        return f"/{self.slug}/"

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

        if self.profile_picture:
            img = Image.open(self.profile_picture.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)

    def get_profile_picture(self):
        if self.profile_picture:
            return "http://127.0.0.1:8000" + self.profile_picture.url
        return ''
