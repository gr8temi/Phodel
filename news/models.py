from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
# Create your models here.

class News(models.Model):
	Title = models.CharField(max_length=50)
	TextField = models.TextField()
	TimePublished = models.DateTimeField(default=timezone.now)
	DatePublished = models.DateTimeField(default=timezone.now)
	def publish(self):
		self.save()

	def __str__(self):
		return self.Title
	

class comment(models.Model):
	Name = models.CharField(max_length=50)
	TextField = HTMLField()
	News_Id = models.ForeignKey(News, on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now)
	def publish(self):
		self.save()

	def __str__(self):
		return self.Name
	
		
	
	