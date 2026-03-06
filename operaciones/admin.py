from django.contrib import admin
from .models import Apartamento, Mantenimiento, Contrato
# Register your models here.


@admin.register(Apartamento)
class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ("apartamentoId", "numero", "habitaciones", "banios", "estado")
    list_filter = ("estado",)
    search_fields = ("numero",)


@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ("mantenimientoId", "descripcion", "prioridad", "estado", "responsable")
    list_filter = ("prioridad", "estado")
    search_fields = ("descripcion",)


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ("contratoId", "inquilino", "apartamento", "estado", "fechaInicio", "fechaFin")
    list_filter = ("estado",)
    search_fields = ("inquilino__nombre", "apartamento__numero")