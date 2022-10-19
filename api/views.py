from django.conf import settings
import requests
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.filters import accountFilter
from api.models import account
from api.serializers import accountSerializer


# Create your views here.
class accountsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = account.objects.all()
    serializer_class = accountSerializer
    filterset_class = accountFilter


class createAccountsViewSet(APIView):

    def get(self, request, *args, **kwargs):
        """Método GET"""
        try:
            response = requests.request('GET', settings.URL_SERVICE, verify=False)
            if response.status_code == 200:
                for data in response.json():
                    account.objects.create(
                        fec_alta = data['fec_alta'],
                        user_name = data['user_name'],
                        codigo_zip = data['codigo_zip'],
                        credit_card_num = data['credit_card_num'],
                        credit_card_ccv = data['credit_card_ccv'],
                        cuenta_numero = data['cuenta_numero'],
                        direccion = data['direccion'],
                        geo_latitud = data['geo_latitud'],
                        geo_longitud = data['geo_longitud'],
                        color_favorito = data['color_favorito'],
                        foto_dni = data['foto_dni'],
                        ip = data['ip'],
                        auto = data['auto'],
                        auto_modelo = data['auto_modelo'],
                        auto_tipo = data['auto_tipo'],
                        auto_color = data['auto_color'],
                        avatar = data['avatar'],
                        fec_birthday = data['fec_birthday']
                    )
                return Response('Se ejecuto exitosamente', status=status.HTTP_200_OK)
            else:
                return Response('Se presento un error al consultar la información' + str(response.text), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response('Se presento el siguiente error' + str(e), status=status.HTTP_400_BAD_REQUEST)
