from django.db import models

# Create your models here.
class account(models.Model):


    fec_alta = models.CharField('Fecha alta', max_length=16)
    user_name = models.CharField('Nombre de usuario', max_length=16)
    codigo_zip = models.CharField('Código ZIP', max_length=16)
    credit_card_num = models.CharField('Número tarjeta de crédito', max_length=16)
    credit_card_ccv = models.CharField('CCV tarjeta de crédito', max_length=16)
    cuenta_numero = models.CharField('Número cuenta', max_length=16)
    direccion = models.CharField('Dirección', max_length=16)
    geo_latitud = models.CharField('Latitud', max_length=16)
    geo_longitud = models.CharField('Longitud', max_length=16)
    color_favorito = models.CharField('Color favorito', max_length=16)
    foto_dni = models.CharField('Foto', max_length=16)
    ip = models.CharField('IP', max_length=16)
    auto = models.CharField('Auto', max_length=16)
    auto_modelo = models.CharField('Modelo Auto', max_length=16)
    auto_tipo = models.CharField('Tipo Auto', max_length=16)
    auto_color = models.CharField('Color Auto', max_length=16)
    avatar = models.CharField('Avatar', max_length=16)
    fec_birthday = models.CharField('Fecha Nacimiento', max_length=16)


    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
    
    def __str__(self):
        return str(self.user_name)