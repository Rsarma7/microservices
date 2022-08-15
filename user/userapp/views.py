from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializer import UserSerilizer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    queryset = User.objects.all()
    serializer_class = UserSerilizer

    permission_classes_by_action = {
        'lists': [AllowAny],
        'creates': [AllowAny],
        'update': [AllowAny],
        'destroy': [AllowAny],
        }

    def creates(self, request, args, *kwargs):
        return super(UserViewSet,self).create(request, args, *kwargs)

    def lists (self, request, args, *kwargs):
        return super(UserViewSet,self).list(request, args, *kwargs)

    def update(self, request, args, *kwargs):
        return super(UserViewSet,self).update(request, args, *kwargs)
    
    def destroy(self, request, args, *kwargs):
        return super(UserViewSet,self).destroy(request, args, *kwargs)
    
    

    def get_permissions(self):
        try: 
            permissions=[permission() for permission in self.permission_classes_by_action[self.action]]
            print(f'permissions= {permissions}')
            return permissions
        except KeyError:
            permissions=[permission() for permission in self.permission_classes]
            print(f' [ERROR] Default permissions= {permissions}')
            return permissions
