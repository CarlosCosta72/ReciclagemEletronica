from django.db import models

class componente(models.Model):
    nome = models.CharField(max_length=100, null = False, blank = False )
    quantidade = models.IntegerField(default = 0)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

