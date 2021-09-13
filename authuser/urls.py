from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('register/',views.signUpForm, name="register"),    
    path('login/',views.HandleLogin.as_view(), name="login"),
    path('logout/',views.logout_user, name="logout"),
    path('standard/',views.StandardListView.as_view(), name="standard_list"),
    path('<slug:slug>/' ,views.SubjectListView.as_view(), name="subject_list"),
    path('<str:standard>/<slug:slug>/' ,views.LessonListView.as_view(), name="lesson_list"),
    path( '<str:standard>/<str:slug>/create/' ,views.LessonCreateView.as_view(), name="lesson_create" ),
    
    path( '<str:standard>/<str:subject>/<slug:slug>/' ,views.LessonDetailView.as_view(), name="lessondetail" ),
    path( '<str:standard>/<str:subject>/<slug:slug>/update/' ,views.LessonUpdateView.as_view(), name="lesson_update" ),
    path( '<str:standard>/<str:subject>/<slug:slug>/delete/' ,views.LessonDeleteView.as_view(), name="lesson_delete" ), 
    


]
