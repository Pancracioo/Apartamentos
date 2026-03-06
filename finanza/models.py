from django.db import models


class Pago(models.Model):
    METODO = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
    ]
    ESTADO = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('atrasado', 'Atrasado'),
    ]
    pagoId = models.AutoField(primary_key=True)
    contrato = models.ForeignKey(
        'operaciones.Contrato',
        on_delete=models.CASCADE,
        related_name='pagos'
    )
    metodo = models.CharField(max_length=20, choices=METODO, default='efectivo')
    montoTotal = models.DecimalField(max_digits=10, decimal_places=2)
    periodo = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, choices=ESTADO, default='pendiente')
    def __str__(self):
        return f'Pago {self.pagoId} | {self.montoTotal} | {self.estado} | {self.periodo}'


class Gasto(models.Model):
    ESTADO = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('atrasado', 'Atrasado'),
    ]
    gastoId = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    coste = models.DecimalField(max_digits=10, decimal_places=2)
    periodo = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, choices=ESTADO, default='pendiente')
    def __str__(self):
        return f'{self.descripcion} | {self.coste}'


class GastoApartamento(models.Model):
    ESTADO = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('atrasado', 'Atrasado'),
    ]
    gastoApartamentoId = models.AutoField(primary_key=True)
    gasto = models.ForeignKey(
        'finanza.Gasto',
        on_delete=models.CASCADE
    )
    apartamento = models.ForeignKey(
        'operaciones.Apartamento',
        on_delete=models.CASCADE
    )
    monto_asignado = models.DecimalField(max_digits=10, decimal_places=2)
    pagoEstado = models.CharField(max_length=20, choices=ESTADO, default='pendiente')
    def __str__(self):
        return f'{self.gasto} | {self.apartamento}'