from django.db import models
from datetime import datetime

from django.contrib.auth.models import User


# Create your models here.

class ItemAgenda(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    usuario = models.ForeignKey(User)
    participantes = models.ManyToManyField(User, 
                                           related_name='item_participantes')
    
def envia_email(**kwargs):
    try:
        item = kwargs['instance']
    except KeyError:
        return
    for participante in item.participantes.all():
        if participante.email:
            dados = (item.titulo,
                     datetime.strftime(item.data, "%d/%m/%Y"),
                     item.hora)
            participante.email_user(
                subject="[evento] %s dia %s as %s" % dados,
                message="Evento: %s\nDia: %s\nHora: %s" % dados,
                from_email=item.usuario.email
)

models.signals.post_save.connect(envia_email,
                                 sender=ItemAgenda,
                                 dispatch_uid="agenda.models.ItemAgenda")