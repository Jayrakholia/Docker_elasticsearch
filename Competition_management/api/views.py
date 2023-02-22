from api.serializers import UserSerializer
from api.serializers import CompetitionSerializer
from api.serializers import EntrySerializer
from api.models import User
from api.models import Competition
from api.models import Entry
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

@csrf_exempt
#USER CRUD
@api_view(['GET','POST','DELETE','PUT'])
def user_curd(request, id = None):
     user_id = id
     if request.method == 'GET': #get data
          if id is not None:
               usr = User.objects.get(id = user_id)
               serializers = UserSerializer(usr)
               # json_data = JSONRenderer().render(serializers.data)
               # return HttpResponse(json_data, content_type ='application/json')
               return Response(serializers.data)
          usr = User.objects.all()
          serializers = UserSerializer(usr, many= True)
          return Response(serializers.data)
     
     if request.method == 'POST':  #add data
          serializers = UserSerializer(data=request.data)
          if serializers.is_valid():
               serializers.save()
               return Response("Add Sucessfully !")
          return Response(serializers.errors)   
          
     if request.method == 'PUT':   #update data
          if id is not None:
               usr = User.objects.get(id = user_id)
               serializers = UserSerializer(usr, data=request.data, partial=True)
               if serializers.is_valid():
                    serializers.save()
               return Response("update Sucessfully !")
          return Response(serializers.errors)
     
     if request.method == 'DELETE': #delete data
          if id is not None:
               usr = User.objects.get(id = user_id)
               usr.delete()
               return Response("delete sucessfully !")
          return Response("ID is NOT FOUND !")

@csrf_exempt
#COMPETITION CRUD
@api_view(['GET','POST','DELETE','PUT'])
def competition_curd(request, id = None):
     competition_id = id
     if request.method == 'GET':  #get data
          if id is not None:
               com = Competition.objects.get(id = competition_id)
               serializers = CompetitionSerializer(com)
               # json_data = JSONRenderer().render(serializers.data)
               # return HttpResponse(json_data, content_type ='application/json')
               return JsonResponse(serializers.data, safe=False)
          com = Competition.objects.all()
          serializers = CompetitionSerializer(com, many= True)
          return JsonResponse(serializers.data, safe=False)

     if request.method =='POST':  #add data
          serializers = CompetitionSerializer(data=request.data)
          if serializers.is_valid():
               serializers.save()
               return JsonResponse("Add Sucessfully !",safe=False)
          return JsonResponse(serializers.errors,safe=False)
     
     if request.method =='PUT':  #update data
          if id is not None:
               com=Competition.objects.get(id=competition_id)
               serializers=CompetitionSerializer(com,partial=True,data=request.data)
               if serializers.is_valid():
                    serializers.save()
                    return JsonResponse("Update Successfully !",safe=False)
               return JsonResponse(serializers.errors,safe=False)
     
     if request.method =='DELETE': #delete data
          if id is not None:
               com= Competition.objects.get(id=competition_id)
               com.delete()
               return JsonResponse("Delete Successfully !",safe=False)
          return JsonResponse("ID is NOT FOUND !")
          

@csrf_exempt
#ENTRY CRUD
@api_view(['GET','POST','DELETE','PUT'])
def entry_curd(request,id=None):
     entry_id = id
     if request.method == 'GET': #get data
          if id is not None:
               ent = Entry.objects.get(id=entry_id)
               serializers = EntrySerializer(ent)
               return JsonResponse(serializers.data,safe=False)
          ent = Entry.objects.all()
          serializers = EntrySerializer(ent, many= True)
          return JsonResponse(serializers.data, safe=False)
     
     if request.method =='POST': #add data
          serializers = EntrySerializer(data=request.data)
          if serializers.is_valid():
               serializers.save()
               return JsonResponse("Added Successfully !",safe=False)
          return JsonResponse(serializers.errors,safe=False)
     
     if request.method =='PUT': #update data
          if id is not None:
               ent= Entry.objects.get(id=entry_id)
               serializers= EntrySerializer(ent,data=request.data,partial=True)
               if serializers.is_valid():
                    serializers.save()
                    return JsonResponse("Update Successfully!",safe=False)
               return JsonResponse(serializers.errors,safe=False)
          
     if request.method =='DELETE': #delete data
          if id is not None:
               ent = Entry.objects.get(id=entry_id)
               ent.delete()
               return JsonResponse("Delete Successfully!",safe=False)
          return JsonResponse("ID is NOT FOUND !",safe=False)
          
