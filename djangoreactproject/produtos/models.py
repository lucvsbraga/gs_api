from django.db import models


class Produto (models.Model):
    nome = models.CharField("Nome", max_length=255)
    preco = models.FloatField(blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return self.nome
