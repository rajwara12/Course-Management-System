from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models import fields
 
 
from . models import *

def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} is already taken."),params = {'value':value})

class UserForm(UserCreationForm):
    email = forms.EmailField(validators = [validate_email])
    class Meta:
        model = User 
        fields=['username','first_name','last_name','password1','password2'] 

        labels={
            'password1':'Password',
            'password2':'Confirm Password',
        }


class UserInfoPage(forms.ModelForm):

     

    bio = forms.CharField(required=False)
    parent='parent'
    student='student'
    user_types = [
         
        (student,'student'),
        (parent,'parent'),
    ]
    user_type = forms.ChoiceField(required=True, choices = user_types )
    class Meta:
        model=User_Profile
        fields=[ 'bio','profile_image','user_type']



class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        # fields='__all__'
        fields=[ 'position','name','description','lesson_video','lesson_image','ppt','notes']