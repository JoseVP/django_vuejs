# -*- encoding: utf-8 -*-
from rest_framework import serializers

from juego.models import Partida

__author__ = "Jose Maria Valenzuela Perez"


class DynamicFieldsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(serializers.ModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class PartidaSerializer(DynamicFieldsSerializer):
    class Meta:
        model = Partida
        fields = serializers.ALL_FIELDS

# --------------------Este producto es una aplicación software propiedad de NARANJO INTELLIGENT SOLUTIONS S.L.---------------------
# ---------------------------------------------------------------------------------------------------------------------------------
# Tanto este producto como los manuales y cualquier otro tipo de material entregado al cliente directa o indirectamente
# por NARANJO INTELIGENT SOLUTIONS S.L., incluyendo sus correspondientes copyrights u otros derechos de propiedad industrial
# o intelectual, son propiedad de  NARANJO INTELIGENT SOLUTIONS S.L. y están protegidos por las leyes de propiedad intelectual
# (Real Decreto Legislativo 1/1996, de 12 de abril, por el que se aprueba el texto refundido de la Ley de Propiedad Intelectual)
# y por las disposiciones comunitarias y tratados internacionales que le sean de aplicación.
# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------
# Queda prohibida la copia, reproducción, alquiler, o distribución a terceras personas, con finalidad comercial o de otra índole
# del  Software, ya sea parcial o en su totalidad, así como su uso en general de forma no acorde a la naturaleza del Software.
# Cualquier uso de los Contenidos del Software debe hacerse con carácter estrictamente personal, privado, y sin fines comerciales
# o lucrativos, a menos que NARANJO INTELIGENT SOLUTIONS S.L. indique explícitamente lo contrario. En ningún momento podrá ser
# objeto de copia, alteración, o descompilación el código fuente mediante técnicas de ingeniería inversa, o cualquier otra técnica.
# ---------
