from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from ..models.subject_model import SubjectModel
from ..serializers.subject_serializer import SubjectSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def list_subject(request):
    if request.method == 'GET':
        subjects = SubjectModel.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    
@csrf_exempt
def subject_detail(request, id):
    try :
        subject = SubjectModel.objects.get(id=id)
    except SubjectModel.DoesNotExist : 
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer =  SubjectSerializer(subject)
        return JsonResponse(serializer.data)
