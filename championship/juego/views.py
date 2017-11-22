# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.translation import ugettext as _


from juego.models import Partida
from juego.serializers import PartidaSerializer


class PartidaViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer
    http_method_names = ['get', 'post', 'delete', 'put']


    # @detail_route(methods=['get'])
    def list(self, request):
        if request.user.has_perm('juego.add_partida'):

            arreglo_srz = PartidaSerializer(Partida.objects.all(), many=True)
            return Response(arreglo_srz.data, status.HTTP_200_OK)

        else:
            return Response({'mensaje': 'permisos insuficientes'}, status.HTTP_403_FORBIDDEN)


    # @detail_route(methods=['post'])
    def create(self, request):
        if request.user.has_perm('juego.add_partida'):
            partida_srz = PartidaSerializer(data=request.data)
            if partida_srz.is_valid():
                partida_srz.save()
                return Response({
                    'mensaje': 'Partida creada correctamente',
                }, status.HTTP_201_CREATED)
            else:
                return Response(partida_srz.errors, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'mensaje': 'permisos insuficientes'}, status.HTTP_403_FORBIDDEN)


    # @detail_route(methods=['get'], url_path='get')
    def retrieve(self, request, pk=None):
        # if request.user.has_perm('juego.consultar_partida'):
        partida = Partida.objects.get(pk=pk)
        partida_srz = PartidaSerializer(partida)

        return Response(partida_srz.data, status.HTTP_200_OK)
        # else:
            # return Response({'mensaje': _('permisos insuficientes')}, status.HTTP_403_FORBIDDEN)


    # @detail_route(methods=['patch'])
    def update(self, request, pk=None):
        if request.user.has_perm('juego.change_partida'):
            partida = Partida.objects.get(pk=pk)
            partida_srz = PartidaSerializer(partida, data=request.data)
            if partida_srz.is_valid():
                try:
                    partida_srz.save()
                except ValidationError as e:
                    return Response({'mensaje': str(e)}, status.HTTP_406_NOT_ACCEPTABLE)
                return Response({
                    'mensaje': 'Partida modificado correctamente',
                }, status.HTTP_200_OK)
            else:
                return Response(partida_srz.errors, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'mensaje': _('permisos insuficientes')}, status.HTTP_403_FORBIDDEN)


    
    # @detail_route(methods=['delete'], url_path='delete')
    def destroy(self, request, pk=None):
        if request.user.has_perm('juego.delete_partida'):
            partida = Partida.objects.get(pk=pk)
            partida.delete()
            return Response({'mensaje': 'Partida eliminado correctamente'}, status.HTTP_200_OK)

        else:
            return Response({'mensaje': 'permisos insuficientes'}, status.HTTP_403_FORBIDDEN)
