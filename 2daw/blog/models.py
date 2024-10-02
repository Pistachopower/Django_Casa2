from django.db import models

# Create your models here.


from django.conf import settings
from django.db import models
from django.utils import timezone

#Siempre deben heredar de la clase padre Model para indicar que es un modelo
class Post(models.Model): 
    #Indicamos que es una clave foránea que hace referencia a otro modelo
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    #Indicamos que es de tipo char con un máximo de 200 caracteres
    title = models.CharField(max_length=200)
    
    #Indicamos que es de tipo Texto
    text = models.TextField()
    
    #Indicamos que es de tipo DateTime
    created_date = models.DateTimeField(default=timezone.now)
    
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
