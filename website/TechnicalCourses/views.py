from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from .models import AllCourses


def Courses(request):
    ac= AllCourses.objects.all()
    template = loader.get_template('TechnicalCourses/Courses.html')
    context = {    
        'ac':ac,
    }
    return HttpResponse(template.render(context,request) )


def Details(request,course_id):
    try:
        course = AllCourses.objects.get(pk=course_id)
    except AllCourses.DoesNotExist:
        raise Http404("Course Not Available")

    return render(request,'TechnicalCourses/details.html',{'course':course})
