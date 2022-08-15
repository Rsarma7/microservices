from django.shortcuts import render

# Create your views here.
from .models import todo
from rest_framework import viewsets
from .serializers import todoSerilizer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
import requests 
from django.http import JsonResponse
# Create your views here.

class todoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    queryset = todo.objects.all()
    serializer_class = todoSerilizer

    permission_classes_by_action = {
        'lists': [IsAdminUser],
        'creates': [AllowAny],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
        }

    def creates(self, request, args, *kwargs):
        todo_des = self.request.__dict__['todo_des']
        username = self.request.__dict__['username']
        created_date = self.request.__dict__['created_date']
       # return super(todoViewSet,self).create(request, args, *kwargs)
        url= 'http://127.0.0.1:8000/User/'
        user= requests.get(url)
        if user: 
            for i in user:
                if i.username==username:
                    break
            data={
                "todo_des" : todo_des,
                "username" : username,
                "created_date" : created_date
            }
            serializer = todoSerilizer(data = data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse (serializer.data, status = 201)

                
    def lists (self, request, args, *kwargs):
        return super(todoViewSet,self).list(request, args, *kwargs)

    def update(self, request, args, *kwargs):
        return super(todoViewSet,self).update(request, args, *kwargs)
    
    def destroy(self, request, args, *kwargs):
        return super(todoViewSet,self).destroy(request, args, *kwargs)
    
    

    def get_permissions(self):
        try: 
            permissions=[permission() for permission in self.permission_classes_by_action[self.action]]
            print(f'permissions= {permissions}')
            return permissions
        except KeyError:
            permissions=[permission() for permission in self.permission_classes]
            print(f' [ERROR] Default permissions= {permissions}')
            return permissions
