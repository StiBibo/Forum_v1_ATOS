from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from ..models.message_model import MessageModel
from ..serializers.message_serializer import MessageSerialiizer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def list_message(request):
    if request.method == 'GET':
        messages = MessageModel.objects.all()
        serializer = MessageSerialiizer(messages, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerialiizer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

