from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Calls(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField('Titulo', max_length=100)
    title_group_name = models.CharField('Titulo do Grupo', max_length=100) # title com uuid
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calls')
    completed_service = models.BooleanField("Atendimeno Finalizado")
    attendant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answered_calls')
    messages = models.JSONField("Mensagens")

