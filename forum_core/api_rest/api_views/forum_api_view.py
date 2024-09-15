from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from ..models.forum_model import ForumModel
from ..serializers.forum_serializer import ForumSerialiizer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def list_forum(request):
    if request.method == 'GET':
        forums = ForumModel.objects.all()
        serializer = ForumSerialiizer(forums, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ForumSerialiizer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    
@csrf_exempt
def forum_detail(request, id):
    try :
        forum = ForumModel.objects.get(id=id)
    except ForumModel.DoesNotExist : 
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer =  ForumSerialiizer(forum)
        return JsonResponse(serializer.data)
