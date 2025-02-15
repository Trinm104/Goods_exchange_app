from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from authentication.models import Course

from django.shortcuts import redirect
# Create your views here.

def products (request):
    return render(request, 'products/index.html')

def courses(request):
    courses = Course.objects.all()  # Lấy tất cả các khóa học
    template = loader.get_template('products/courses.html')  # Template hiển thị
    context = {
        'courses': courses,  # Đổi 'course' thành 'courses' để khớp với template
    }
    return HttpResponse(template.render(context, request))


def edit_course(request):
    course = Course.objects.get(id = 1)
    template = loader.get_template('products/course-edit.html')
    context = {
        'course': course,
    }
    return HttpResponse(template.render(context, request))

def CourseNew(request):
    if request.method == "POST":
        print("POST data:", request.POST)  # In dữ liệu POST để kiểm tra
        form = CourseNewForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Xác nhận form hợp lệ
            return HttpResponseRedirect("/courses")
        else:
            print("Form errors:", form.errors)  # Hiển thị lỗi nếu có
    else:
        form = CourseNewForm()

    template = loader.get_template('products/course-new.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

    
