from django.db import models

# Create your models here.

class Domicilio(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)

    def __str__(self):
        return self.calle + ", " + self.ciudad + " - " + self.codigo_postal


class Persona(models.Model):
    id = models.AutoField(primary_key=True) #No es necesario añadirlo pues Django lo añade automáticamente
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()
    #Para añadir una llave foránea se utiliza el campo ForeignKey, su sintaxis es models.ForeignKey()
    """
    to: El modelo al que se relaciona (por ejemplo, Categoria).
    on_delete: Qué hacer cuando el objeto relacionado se elimina. Ejemplos:
        models.CASCADE: Borra también los objetos relacionados.
        models.PROTECT: Impide borrar si hay objetos relacionados.
        models.SET_NULL: Pone el campo en NULL si se borra el objeto relacionado (requiere null=True).
        models.SET_DEFAULT: Pone el valor por defecto.
        models.SET(...): Pone un valor específico o llama a una función.
        models.DO_NOTHING: No hace nada (puede causar errores de integridad).
    related_name: Nombre para acceder a la relación inversa desde el modelo relacionado.
    null: Permite que el campo sea nulo en la base de datos.
    blank: Permite que el campo esté vacío en formularios.
    default: Valor por defecto.
    limit_choices_to: Limita las opciones disponibles en el admin.
    verbose_name: Nombre legible para el campo.
    help_text: Texto de ayuda para el campo.
    """

    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE, null=True, blank=True) #Relación muchos a uno
    #Siempre que se cree una nuevo modelo se usa makemigrations y luego migrate

    #Se modifica como se ve en admin
    def __str__(self):
        return self.nombre + " (" + str(self.edad) + ")" + " - " + self.email
