from django.contrib import admin
from catalogo.models import Estado, Institucion, Facultad
# Register your models here.

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_estado',)

class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('nombre_universidad', 'nombre_rector')

class FacultadAdmin(admin.ModelAdmin):
    list_display = ('entidad', 'institucion', 'region', 'tipo', 'estatus',
                    'acreditacion', 'nombre_escuela', 'nombre_campus',
                    'nombre_director', 'mail_contacto', 'domicilio',
                    'sitio_web', 'telefono')

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Facultad, FacultadAdmin)
