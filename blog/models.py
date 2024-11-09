from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator
from django.db import models
# from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)


    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("category_post", args=[self.slug])
    

class Publishmeneger(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super(Publishmeneger, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique_for_date='publish', null=True)
    # author = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True)

    # video = models.URLField(blank=True, null=True) 
    video = models.FileField(upload_to='videos/')  # Faylni "videos/" papkasiga yuklash
    photo = models.ImageField(upload_to="photos", null=True, blank=True)
    date_uploaded = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    body =  models.CharField(max_length=100000)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = Publishmeneger()
    uploaded_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-publish',)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
    



class CommentPospt(models.Model):
    # author = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.author}  ->  {self.created}"


class Contact(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()


    def __str__(self) -> str:
        return self.username