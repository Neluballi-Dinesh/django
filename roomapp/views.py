from django.shortcuts import render
from .models import studentData
from django.http import HttpResponse

def studentdata(request):
    if request.method=='GET':
        return render(request,'studentData.html')
    else:
        studentData(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        course=request.POST['course'],
        mobile=request.POST['mobile'],
        location=request.POST['location']
        ).save()
        return render(request,'studentData.html')
