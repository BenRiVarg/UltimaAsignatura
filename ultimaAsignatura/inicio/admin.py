from django.contrib import admin

from .models import MaterialesPractica
from .models import Empleados

# Register your models here.

class AdministrarMP(admin.ModelAdmin):
    #readonly_fields=('id')
    list_display=('nombrePractica','grupo','hora','solicitante')
    search_fields=('nombrePractica','grupo','hora','solicitante')
       # date_hierarchy='created'
    #list_filter=('carrera','turno')

    

admin.site.register(MaterialesPractica,AdministrarMP)



class AdministrarEmpleado(admin.ModelAdmin):
    list_display=('foto','nombreEmpleado','skills','telefono','domicilio')
    search_fields=('id','nombreEmpleado','skills','telefono')
    list_filter=('skills',)

    

admin.site.register(Empleados,AdministrarEmpleado)