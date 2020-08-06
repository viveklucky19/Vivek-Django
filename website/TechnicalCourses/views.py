from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from .models import AllCourses,details


def Courses(request):
    ac= AllCourses.objects.all()
    template = loader.get_template('TechnicalCourses/Courses.html')
    context = {    
        'ac':ac,
    }
    return HttpResponse(template.render(context,request) )


def Details(request,course_id):
    course = get_object_or_404(AllCourses,pk=course_id)
    # try:
    #     course = AllCourses.objects.get(pk=course_id)
    # except AllCourses.DoesNotExist:
    #     raise Http404("Course Not Available")

    return render(request,'TechnicalCourses/details.html',{'course':course})


def YourChoice(request,course_id):

    course= get_object_or_404(AllCourses,pk=course_id)
    try:
        sel_ct =course.details_set.get(pk=request.POST['choice'])
    except (KeyError,AllCourses.DoesNotExist):
        return render (request ,'TechnicalCourses/details.html',{'course':course,
        'error_message':"Select a valid option"})
    else:
        sel_ct.your_choice = True
        sel_ct.save()
        return render(request,'TechnicalCourses/details.html',{'course':course})

