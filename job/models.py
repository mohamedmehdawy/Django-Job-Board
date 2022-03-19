from concurrent.futures import thread
from tkinter import CASCADE
from django.db import models
# importing slugify from django
from django.utils.text import slugify
# Create your models here.
def image_upload(instance, file_name):

    extension_name = file_name.split(".")[1]
    return f"jobs/{instance.id}.{extension_name}"
class Job(models.Model):
    JOB_NUTURE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]
    title = models.CharField(max_length=100)
    # location
    job_nature = models.CharField(max_length=15, choices=JOB_NUTURE_CHOICES)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload) 
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    coverletter = models.TextField(max_length=500)
    created_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name