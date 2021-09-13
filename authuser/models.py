from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=400, blank=True)
    profile_image = models.ImageField(upload_to="images", blank=True)

    teacher='teacher'
    parent='parent'
    student='student'
    user_types = [
        (teacher,'teacher'),
        (student,'student'),
        (parent,'parent'),
    ]
    user_type = models.CharField(max_length=100, choices= user_types, default=student)

    def __str__(self)  :
        return self.user.username

class Standard(models.Model):
    name= models.CharField(max_length=300)
     
    slug= models.SlugField(blank=True  )
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Standard,self).save( *args, **kwargs)        

    def __str__(self)  :
        return self.name    

class Subject(models.Model):

     
    name = models.CharField(max_length=300, unique=False)
    standard= models.ForeignKey(Standard,on_delete=models.CASCADE, related_name='subjects') 
    slug = models.SlugField(blank=True  )
    description = models.TextField()
    subject_image = models.ImageField(upload_to="subjectimages", blank=True)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Subject,self).save( *args, **kwargs)        

    def __str__(self)  :
        return self.name  

     


class Lesson(models.Model):
    standard= models.ForeignKey(Standard,on_delete=models.CASCADE )
    created_by= models.ForeignKey(User,on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    subject= models.ForeignKey(Subject,on_delete=models.CASCADE, related_name='lessons')
    name= models.CharField(max_length=300, unique=False)
    position = models.PositiveSmallIntegerField(verbose_name="Chapter no. ")
    slug= models.SlugField(blank=True  )
    description = models.TextField()
    lesson_video = models.FileField(upload_to="subjectimages", blank=True)
    lesson_image = models.ImageField(upload_to="subjectimages", null=True, blank=True)
    ppt = models.FileField(upload_to="subjectimages", blank=True, verbose_name="Presentations")
    notes = models.FileField(upload_to="subjectimages", blank=True)

    class Meta:
        ordering=['position']

     


    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Lesson,self).save( *args, **kwargs)    
        
            

    def __str__(self)  :
        return self.name                  