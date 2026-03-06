from django.contrib import admin
from .models import Usuario, Inquilino
# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("usuarioId", "nombre", "permisos", "fecha_reg")
    search_fields = ("nombre",)
    list_filter = ("permisos",)


@admin.register(Inquilino)
class InquilinoAdmin(admin.ModelAdmin):
    list_display = ("inquilinoId", "nombre", "apellido", "apartamento", "fecha_reg")
    search_fields = ("nombre", "apellido", "cedula")
    list_filter = ("fecha_reg",)