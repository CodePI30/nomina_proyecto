from django.db import models

class Nomina(models.Model):
    rnc_empresa = models.CharField(max_length=9)
    fecha_proceso = models.CharField(max_length=100)
    codigo_cliente = models.CharField(max_length=10)
    moneda = models.CharField(max_length=3)
    cuenta_bancaria_empresa = models.CharField(max_length=20)
    cuenta_bancaria_empleado = models.CharField(max_length=20)
    cedula_empleado = models.CharField(max_length=11)
    monto_pagar = models.CharField(max_length=10)
    referencia = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina'
