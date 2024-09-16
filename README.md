# Forum_v1_ATOS
Mise en place d'un projet de gestion d'un forum

Pour la mise en place de notre projet, nous avons implementer des api restFul pour nos fonstionnalités.

# Locigiel utilisé

Pour la création de nos API, nous avons :
-Dans un dossier que nous avons creer, on a creer notre environnement 'python -m venv nomenvironnement' et nous l'avons activé
-Installer django(en invite de commande 'pip install django'); par la suite creer un projet django 'django-admin startproject nomprojet'
-Nous avons creer deux application une application de Base et une application que nous avons nommé api. Par la suite nous avons declaré nos deux application dans le setting.py
'INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # app
    'rest_framework',

    # APPS INSTALLED
    'api_rest.apps.ApiRestConfig',
    'base.apps.BaseConfig',


]'
Pour l'utilisation des API nous avons installé django rest-framework et nous l'avons declaré dans notre setting comme nos applications
-Nous avons faire la configuration de notre base de donnée dans le fichier setting. Nous utilisons postgresql
'DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'forumV1',
        'USER':'postgres',
        'PASSWORD':'armelle',
        'HOST':'localhost',
        'PORT':'5432',
    }
}'
-Nous avons definir notre url dans le fichier urls du projet django
'    path('api/', include('api_rest.urls')),'

# Creation de nos API
Pour la création de nos fonctionnalites, nous allons utilise les fonctions pour la création de nos API.
- Creation de nos modeles
Nous avons creer trois fichier(forum_model,subject_model,message_model) qui vont hériter des classes abstract(DateTimeModel, NameDateTimeModel).
Nous allons faire 'python manage.py makemigrations'et 'python manage.py migrate' pour la créationde nos differents tables 
- Nous avons creer un dossier serializer qui contient trois fichiers(forum_serializer,subject_serializer,message_serializer). Chacun de ces fichiers va importer son modele; ces fihier ce comporte comme des formulaire liée.
- Nous allons creer un dossier api_view pour la creation de nos differentes views 

'from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from api.models.forum_model import ForumModel
from api.serializers.forum_serializer import ForumSerializer

 @csrf_exempt
 def forum_list(request):
     if request.method == 'GET':
         forums = ForumModel.objects.all()
         serializer = ForumSerializer(forums, many=True)
         return JsonResponse(serializer.data, safe=False)
    
     elif request.method == 'POST':
         data = JSONParser().parse(request)
         serializer = ForumSerializer(data=data)
         if serializer.is_valid():
             serializer.save()
             return JsonResponse(serializer.data, status=201)
         return JsonResponse(serializer.errors, status=400) '
Dans notre exemple ci dessous, nous avons creer deux requete ('POST' pour la creation et une 'GET' pour lister)

- Dans le fichier urls que nous avons appeler nos differents views

# execution 
'python manage.py runserver ' Pour exceuter le projet
