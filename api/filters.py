from django_filters import rest_framework as filters

from api.models import account


class accountFilter(filters.FilterSet):
    class Meta:
        model = account
        fields = {
            'fec_alta': ['exact', 'contains'],
            'user_name': ['exact', 'contains'],
            'codigo_zip': ['exact', 'contains'],
            'credit_card_num': ['exact', 'contains'],
            'credit_card_ccv': ['exact', 'contains'],
            'cuenta_numero': ['exact', 'contains'],
            'direccion': ['exact', 'contains'],
            'geo_latitud': ['exact', 'contains'],
            'geo_longitud': ['exact', 'contains'],
            'color_favorito': ['exact', 'contains'],
            'foto_dni': ['exact', 'contains'],
            'ip': ['exact', 'contains'],
            'auto': ['exact', 'contains'],
            'auto_modelo': ['exact', 'contains'],
            'auto_tipo': ['exact', 'contains'],
            'auto_color': ['exact', 'contains'],
            'avatar': ['exact', 'contains'],
            'fec_birthday': ['exact', 'contains'],
            'id': ['exact', 'contains'],
        }
        ordering_fields  = ('id')