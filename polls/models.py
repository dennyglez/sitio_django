import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
# Modelos Question y Choice para el primer sitio de voto y visualización de encuestas.
class Question(models.Model):
    question_text = models.CharField(max_length=200) #  Pregunta / argumento: max_length
    pub_date = models.DateTimeField("date published") # Fecha de publicación
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200) # Texto de elección
    votes = models.IntegerField(default=0) # Votos
    def __str__(self):
        return self.choice_text 
    

    

