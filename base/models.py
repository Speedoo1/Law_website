from ckeditor.fields import *
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.db import models
from num2words import num2words


# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=True, max_length=200)
    companyname = models.CharField(max_length=200, )
    email = models.EmailField()
    about = RichTextUploadingField(blank=True, null=True, )
    tel = models.CharField(max_length=20, null=True, blank=True)
    time = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)


class practicearea(models.Model):
    lawtype = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    littleImage = models.CharField(max_length=50, null=True, blank=True)
    learnmore = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.lawtype)


class ourpurpose(models.Model):
    topic = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    littleImg = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.topic)


class expert(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100, null=True)
    consultant = models.CharField(max_length=100, null=True)


class question(models.Model):
    topic = models.CharField(max_length=100, null=True)
    body = models.CharField(max_length=300, null=True)
    collapse = models.CharField(max_length=60, default='#collapse')

    def __str__(self):
        return self.topic

    # class Meta:
    #     # verbose_name = 'property'
    #     verbose_name_plural = 'questions'


class review(models.Model):
    name = models.CharField(max_length=100, null=True)
    profession = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)

