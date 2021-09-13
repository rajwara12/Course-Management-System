import django
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import *
from django.views import View 
from django.contrib.auth import authenticate,   login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import  ListView,  DetailView,  CreateView, UpdateView, DeleteView 
# Create your views here.


class StandardListView(ListView):
    context_object_name="standards"
    model  = Standard
    template_name="registration/standard.html"



class SubjectListView(DetailView):
    context_object_name="standards"
    model  = Standard
    template_name="registration/subject.html"
    
class LessonListView(DetailView):
    context_object_name="subjects"
    model  = Subject
    template_name="registration/subjectdetail.html"    


class LessonDetailView(DetailView):
    context_object_name="lessons"
    model  = Lesson
    template_name="registration/lessondetail.html"     



class LessonCreateView(CreateView):
    form_class=LessonForm
    context_object_name="subject"
    model = Subject
    template_name="registration/lesson_create.html"

    def get_success_url(self ):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('authuser:lesson_list', kwargs={'standard':standard.slug,'slug':self.object.slug})



    def form_valid(self, form, *args, **kwargs) :
        self.object=self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.standard = self.object.standard 
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())
  

class LessonUpdateView(UpdateView):
    fields=[ 'position','name','description','lesson_video','lesson_image','ppt','notes']
    
    model = Lesson
    context_object_name="subject"
    template_name="registration/lesson_update.html"

    def get_success_url(self ):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('authuser:lesson_list', kwargs={'standard':standard.slug,'slug':self.object.slug})



class LessonDeleteView(DeleteView):
     
    
    model = Lesson
    context_object_name="lessons"
    template_name="registration/lesson_delete.html"
    success_url='http://127.0.0.1:8000/'



def home(request):
    return  render(request,'registration/index.html')

def signUpForm(request):
    if request.method=='POST':
        fm1 = UserForm(request.POST)
        fm = UserInfoPage(request.POST)
        
        if fm1.is_valid() and fm.is_valid() :
            user=fm1.save()
            user.save()
            profile = fm.save(commit=False)
            profile.user=user
            profile.save()
            
            
            return redirect('http://127.0.0.1:8000/')
    else:
        fm1=UserForm()
        fm=UserInfoPage()   
    return render(request,'registration/register.html',{'form1':fm1,'form':fm }) 


class HandleLogin(View):
    def get(self,request):
        return render(request,'registration/login.html')
    def post(self,request):
        username = request.POST.get('username')   
        password1 = request.POST.get('password1')
        user = authenticate(username=username,password=password1)
        if user is not None:
            login(request,user)
            messages.success(request,"Your Login sucessfully")
            return redirect('http://127.0.0.1:8000/')
        else:
            messages.error(request,"Invalid Details")
            return redirect('login')

@login_required
def logout_user(request):
        logout(request)
        messages.success(request,"Your Logout sucessfully")
        return redirect('http://127.0.0.1:8000/')     