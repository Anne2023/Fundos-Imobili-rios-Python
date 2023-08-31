from rest_framework import serializers
from api.models import FundoImobiliario


class FundoIobiliarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = FundoImobiliario #define qual modelo esse serializer deve serializar
        fields = [ #define os campos que serão serializado
            'id',
            'codigo',
            'setor',
            'dividend_yild_medio_12m',
            'vacancia_financeira',
            'quantidade_ativos'
        ]