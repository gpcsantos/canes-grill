from django.contrib import admin

from .models import Prato
# Register your models here.

class ListandoPratos(admin.ModelAdmin):
    list_display = [
        'id','nome_prato','categoria', 'tempo_preparo','rendimento', 'publicado'
    ]
    list_display_links = [
        'id','nome_prato',
    ]
    search_fields = ['nome_prato']
    list_editable = ['categoria','publicado']
    ordering = ['-id',]
    list_filter = ['categoria']
    list_per_page = 7
admin.site.register(Prato, ListandoPratos)
