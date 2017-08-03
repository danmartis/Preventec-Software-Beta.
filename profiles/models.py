from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify


from markdown_deux import markdown
from comments.models import Comment

#from utils import get_read_time



class ProfileManager(models.Manager):
	def active(self, *args, **kwargs):
		# Post.objects.all() = super(PostManager, self).all()
		return super(ProfileManager, self).filter(draft=False).filter(inicio_cargo__lte=timezone.now())


def upload_location(instance, filename):
	#filebase, extension = filename.split(".")
	#return "%s/%s.%s" %(instance.id, instance.id, extension)
	ProfileModel = instance.__class__
	new_id = ProfileModel.objects.order_by("id").last().id + 1
	"""
	instance.__class__ gets the model Post. We must use this method because the model is defined below.
	Then create a queryset ordered by the "id"s of each object, 
	Then we get the last object in the queryset with `.last()`
	Which will give us the most recently created Model instance
	We add 1 to it, so we get what should be the same id as the the post we are creating.
	"""
	return "%s/%s" %(new_id, filename)


class Profile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	rut  = models.CharField(max_length=20)
	birthdate = models.DateField()
	avatar = models.ImageField(upload_to='upload_location', 
			null=True, 
			blank=True,
			width_field="width_field", 
			height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	digitalid = models.CharField(max_length=20)
	ultimateupdate = models.DateTimeField()
	cargo = models.ForeignKey('Cargo')
	especialidad = models.ForeignKey('Especialidad')
	inicio_cargo = models.DateField(auto_now=True, auto_now_add=False)
	años_exp = models.IntegerField(null=True, blank=True)
	contrato = models.TextField(null=True, blank=True)
	legales_asoc =  models.TextField(null=True, blank=True)

	objects = ProfileManager()

	def __unicode__(self):
		return self.rut


	def __str__(self):
			return self.rut

	#def get_absolute_url(self):
	#    return reverse("posts:detail", kwargs={"slug": self.slug})

	#def get_api_url(self):
	#    return reverse("posts-api:detail", kwargs={"slug": self.slug})

	class Meta:
		ordering = ["-ultimateupdate",]

	def get_markdown(self):
		content = self.content
		markdown_text = markdown(content)
		return mark_safe(markdown_text)



class Cargo(models.Model):
	nombre = models.TextField(max_length=30)


	def __unicode__(self):
		return self.nombre


	def __str__(self):
			return self.nombre

class Especialidad(models.Model):
	nombre = models.TextField(max_length=30)

	def __str__(self):
			return self.nombre		