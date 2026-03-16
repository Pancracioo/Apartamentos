from django.contrib import admin
from .models import Pago, Gasto, GastoApartamento
# Register your models here.

@admin.register(Pago)
class Pago(admin.ModelAdmin):
    search_fields = ("nombre",)
    list_filter = ("periodo",)


@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    search_fields = ("descripcion",)
    list_filter = ("estado",)


@admin.register(GastoApartamento)
class GastoApartamentoAdmin(admin.ModelAdmin):
    list_display = ("gastoApartamentoId", "gasto", "apartamento", "monto_asignado")
    search_fields = ("apartamento",)
    list_filter = ("apartamento",)