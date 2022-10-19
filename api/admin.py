from django.contrib import admin

from api.models import account

# Register your models here.
class accountAdmin(admin.ModelAdmin):

    list_display = ['fec_alta', 'user_name', 'codigo_zip', 'credit_card_num', 'credit_card_ccv', 'cuenta_numero', 'direccion', 'geo_latitud', 'geo_longitud', 'color_favorito', 'foto_dni', 'ip', 'auto', 'auto_modelo', 'auto_tipo', 'auto_color', 'avatar', 'fec_birthday']

admin.site.register(account, accountAdmin)