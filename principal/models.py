#encoding:utf-8

from django.db import models

from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Receta(models.Model):
	titulo = models.CharField(max_length=100, unique=True)
	ingredientes = models.TextField(help_text='Redacta los ingredientes')
	preparacion = models.TextField(verbose_name='Preparación')
	imagen = models.ImageField(upload_to='recetas', verbose_name='Imágen', blank=True)
	tiempo_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.titulo

	# La siguiente funcion sirve para que las imagenes que ya
	# no estan en uso sean eliminadas, de tal manera que no ocupen espacio.

	def save(self, *args, **kwargs):
	    try:
	        this = Receta.objects.get(id=self.id)
	        if this.imagen != self.imagen:
	            this.imagen.delete()
	    except: pass
	    super(Receta, self).save(*args, **kwargs)	

class Comentario(models.Model):
	receta = models.ForeignKey(Receta)
	texto = RichTextField()
	def __unicode__(self):
		return self.texto


# Ver este link para amplicar campos de User: http://django.es/blog/tag/auth/


# class Perfil(models.Model):
# 	user = models.ForeignKey(User, unique=True)
# 	imagen = models.ImageField(upload_to='usuarios', verbose_name='Imágen')
# 	telefono = models.PositiveIntegerField(null=True, blank=True)


# Este no es el metodo más limpio para ampliar el Modelo User, pero permite que 
# se lo maneke solo como un modelo

User.add_to_class('imagen', models.ImageField(upload_to='usuarios', verbose_name='Imágen'))
User.add_to_class('direccion', models.FloatField(null=True,blank=True))
User.add_to_class('telefono', models.PositiveIntegerField(null=True,blank=True))
User.add_to_class('amigos', models.ManyToManyField('self', symmetrical=True,  blank=True))


