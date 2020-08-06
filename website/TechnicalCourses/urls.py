from django.urls import path
from . import views

app_name='TechnicalCourses'

urlpatterns = [
    path('<int:course_id>/', views.Details, name='details-page'),
    path('', views.Courses, name='home-page'),
    path('<int:course_id>/yourchoice', views.YourChoice, name='yourchoice1'),

]
