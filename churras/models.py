from django.db import models
from datetime import datetime

# Create your models here.

## Esta classe de models se tornará uma tabela no banco de dados
class Prato(models.Model):
    ## serão os campos da tabela (atributos da classe)
    nome_prato = models.CharField(
        max_length=100,
        verbose_name="Nome do Prato",
    )
    ingredientes = models.TextField(
        verbose_name='Ingredientes',
    )
    modo_preparo = models.TextField(
        verbose_name='Modo de Preparo',
    )
    tempo_preparo = models.PositiveIntegerField(
        verbose_name='Tempo de Preparo',
    )
    rendimento = models.CharField(max_length=100, 
        verbose_name='Rendimento'
    )
    categoria = models.CharField(max_length=100,
        verbose_name='Categoria',
    )
    date_prato = models.DateTimeField(
        default=datetime.now, blank=True,
    )

    def __str__(self):
        return self.nome_prato

    class Meta:
        verbose_name = 'Prato'
        verbose_name_plural = 'Pratos' 