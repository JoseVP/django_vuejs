# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class Partida(models.Model):
    INICIADA = 'ini'
    FINALIZADA = 'fin'
    SUSPENDIDA = 'sus'
    ESTADOS_PARTIDA = ((INICIADA,'Iniciada'),
                       (FINALIZADA,'Finalizada'),
                       (SUSPENDIDA,'Suspendida'))
    fecha = models.DateTimeField(default=timezone.datetime.now)
    jugadores = models.ManyToManyField(User,related_name="partidas")
    estado = models.CharField(max_length=3,choices=ESTADOS_PARTIDA,default=INICIADA)


    def __unicode__(self):
        return self.fecha.strftime("%Y-%m-%d %H:%M:%s"),'-',self.get_estado_display()


class Estrella(models.Model):
    TIRADA = "t"
    CAMPEONATO = "c"
    TIPOS_ESTRELLA = ((TIRADA,'Tirada'),(CAMPEONATO,'Campeonato'))

    partida = models.ForeignKey('Partida',related_name="estrellas")
    jugador = models.ForeignKey(User,related_name='estrellas')
    tipo = models.CharField(max_length=1,choices=TIPOS_ESTRELLA,default=CAMPEONATO)

    def __unicode__(self):
        return "%s - %s - %s" %( self.partida.fecha.strftime("%Y-%m-%d %H:%M:%s"),
                                 self.jugador.first_name,
                                 self.get_tipo_display()
                                 )


class Ronda(models.Model):
    fecha = models.DateTimeField(default=timezone.datetime.now)
    partida = models.ForeignKey('Partida', related_name="rondas")
    numero = models.IntegerField(default=0)
    jugadores = models.ManyToManyField(User, related_name="rondas")
    max_aciertos = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s - %d" % (self.partida.fecha.strftime("%Y-%m-%d %H:%M:%s"),
                                 self.numero
                                 )

class Tirada(models.Model):
    NORMAL = 'norm'
    ESPECIAL = 'espe'
    ESTRELLA = 'estr'
    TIPOS_TIRADA =((NORMAL,'Normal'),
                   (ESPECIAL,'Especial'),
                   (ESTRELLA,'Estrella')
                   )


    fecha = models.DateTimeField(default=timezone.datetime.now)
    jugador = models.ForeignKey(User,related_name='tiradas')
    ronda = models.ForeignKey('Ronda',related_name="rondas")
    posicion_ronda = models.IntegerField(default=0)
    acierto = models.NullBooleanField(default=None)
    fallo = models.NullBooleanField(default=None)
    tipo = models.CharField(max_length=4,choices=TIPOS_TIRADA,default=NORMAL)

# Create your models here.
