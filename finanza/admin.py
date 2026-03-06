from django.contrib import admin
from .models import Pago, Gasto, GastoApartamento
# Register your models here.

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ("usuarioId", "nombre", "permisos", "fecha_reg")
    search_fields = ("nombre",)
    list_filter = ("permisos",)

@admin.register(Gasto)
class Gasto(admin.ModelAdmin):
    search_fields = ('descripcion')
    list_filter = ('estado')

@admin.register(GastoApartamento)
class GastoApartamento(admin.ModelAdmin):
    list_display = ('gastoApartamentoId','gasto','apartamento','monto_asignado')
    search_fields = ('apartamento')
    list_filter = ('apartamento')