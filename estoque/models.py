from django.db import models

class Componente(models.Model):
    nome = models.CharField(max_length=100, null = False, blank = False )
    quantidade = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

