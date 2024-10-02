from django.contrib import admin

# Register your models here.
"""
Esta línea importa el modelo Post desde el archivo models.py que 
está en el mismo directorio que el archivo actual (admin.py). 
El punto (.) indica que es una importación relativa.

"""
from .models import Post 

"""
Esta línea registra el modelo Post con el sitio de administración de Django. 
Al hacer esto, le dices a Django que quieres que el modelo Post sea manejable
a través de la interfaz de administración. Esto te permitirá agregar, editar
y eliminar instancias del modelo Post desde el panel de administración de Django.
"""
admin.site.register(Post)

