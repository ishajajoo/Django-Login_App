from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from . serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def HomePage(request):
    #return HttpResponse("Hello world")
    return render(request, 'Login_App/homepage.html')

def IndexPage(request):
    #return HttpResponse("Hello world")
    all_object = Student.objects.all()
    print(all_object)
    return render(request, 'Login_App/index.html')

@csrf_exempt
def AllStudentDetails(request):
    try:
        all_student = Student.objects.all()
    except:
        return HttpResponse("Data not presnet", status = 404)

    if request.method == 'GET':
        students = StudentSerializer(all_student, many=True)
        return JsonResponse(students.data, safe=False)
    
    elif request.method == 'POST':
        input_data = JSONParser().parse(request)
        serializer = StudentSerializer(data = input_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else:
            return HttpResponse("Invalid data", status=400)
        
def SingleStudentDetails(request, pk):
    try:
        student = Student.objects.get(pk = pk)
    except:
        return HttpResponse('Data not found', status = 400)
    
    if request.method == 'GET':
        students_data = StudentSerializer(student)
        return JsonResponse(students_data.data, status = 200)
    
    # elif request.method == 'POST':
    #     input_data = JSONParser().parse(request)
    #     serializer = StudentSerializer(data = input_data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status = 201)
    #     else:
    #         return HttpResponse("Invalid data", status=400)