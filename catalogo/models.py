from django.db import models


# Create your models here.
class Estado(models.Model):
    nombre_estado = models.CharField(max_length=35)

    class Meta:
        ordering = ['nombre_estado']

    def __str__(self):
        return self.nombre_estado


class Institucion(models.Model):
    nombre_universidad = models.CharField(max_length=80)
    nombre_rector = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre_universidad']
        verbose_name_plural = "Instituciones"

    def __str__(self):
        return self.nombre_universidad


class Facultad(models.Model):
    Tipo_Escuela_Choices = (
        ('1', 'Pública'),
        ('2', 'Particular'),
    )

    Estatus_Choices = (
        ('1', 'Acreditada'),
        ('2', 'Aspirante'),
    )

    Region_Choices = (
        ('1', 'Norte'),
        ('2', 'Occidente'),
        ('3', 'Centro'),
        ('4', 'Sur'),
    )

    entidad = models.ForeignKey(Estado)
    institucion = models.ForeignKey(Institucion)
    region = models.CharField(max_length=1, choices=Region_Choices, default=Region_Choices[0][0])
    tipo = models.CharField(max_length=1, choices=Tipo_Escuela_Choices)
    estatus = models.CharField(max_length=1, choices=Estatus_Choices)
    acreditacion = models.CharField(max_length=4, default='2016', blank=True)
    nombre_escuela = models.CharField(max_length=75)
    nombre_campus = models.CharField(max_length=50, blank=True)
    nombre_director = models.CharField(max_length=50)
    mail_contacto = models.EmailField(max_length=50)
    domicilio = models.CharField(max_length=150)
    sitio_web = models.URLField(max_length=100)
    telefono = models.CharField(max_length=40)

    class Meta:
        ordering = ['entidad', 'region', 'institucion', 'nombre_campus']
        verbose_name_plural = "Facultades"

    def __str__(self):
        #return str(Facultad._meta.fields)  # '%s %s %s %s %s' %(self.entidad, self.institucion, self.region, self.nombre_escuela, self.nombre_campus)
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s ' %(self.entidad, self.institucion, self.region, self.tipo, self.estatus, self.acreditacion,
                                                           self.nombre_escuela, self.nombre_campus, self.nombre_director, self.mail_contacto, self.domicilio,
                                                           self.sitio_web, self.telefono)