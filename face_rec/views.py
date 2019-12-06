# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, IdentSerializer
from .utils import face_identification

class UsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.data.get('user')

        # Create an article from the above data
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.firstName + " " + user_saved.lastName)})

class IdentificationView(APIView):
    def post(self, request):
        ident = request.data.get('ident')
        serializer = IdentSerializer(data=ident)
        if serializer.is_valid(raise_exception=True):
            ident_saved = serializer.save()

        users = User.objects.all()

        for user in users.iterator():
            userPhoto = user.photo
            if face_identification.isIdent(userPhoto, ident_saved.photo) == True:
                    return Response({"user": {"firstName": user.firstName,"lastName": user.lastName}})
        
        return Response({"user": {"firstName": "","lastName": ""}})
        