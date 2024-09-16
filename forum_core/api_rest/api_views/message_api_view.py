from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from ..models.message_model import MessageModel
from ..serializers.message_serializer import MessageSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def list_message(request):
    if request.method == 'GET':
        messages = MessageModel.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def message_detail_by_subject(request, id):
    try :
        message = MessageModel.objects.filter(sujet = id)
    except MessageModel.DoesNotExist : 
        return HttpResponse(status=404)
    
    
    if request.method == 'GET':
        serializer =  MessageSerializer(message,many=True)
        return JsonResponse(serializer.data, safe=False)