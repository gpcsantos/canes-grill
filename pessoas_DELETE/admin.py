from django.contrib import admin
from .models import Pessoa

# Register your models here.
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    list_editable =  ['email']
    search_fields = ('nome', 'email')

admin.site.register(Pessoa, PessoaAdmin)