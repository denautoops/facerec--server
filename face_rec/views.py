# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .utils import face_identification, file_utils


class RegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        photo = request.data['photo']
        User.objects.create(first_name=first_name, last_name=last_name, photo=photo)
        return Response(
            {"success": "User '{}' created successfully".format(first_name + ", " + last_name)},
            status=201)


class IdentificationView(APIView):

    def post(self, request):

        ident_photo = file_utils.create_jpeg_file_from_memory(request.data['photo'])

        users = User.objects.all()

        for user in users.iterator():
            photo1 = user.photo
            if face_identification.isIdent(settings.BASE_DIR + photo1.url, ident_photo):
                fn = user.first_name
                ln = user.last_name
                return Response({'firstName': fn, 'lastName': ln})
