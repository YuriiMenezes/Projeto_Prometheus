from django.contrib import admin

# Register your models here.

from .models import Comentario

class ComentarioAdmin(admin.ModelAdmin):

    list_display = ('id', 'nome_comentario', 'email_comentario', 
                    'post_comentario', 'data_comentario',
                    'publicad_comentario', )

    list_editable = ('publicad_comentario', )

    list_display_links = ('id', 'nome_comentario', 'email_comentario', )                


admin.site.register(Comentario, ComentarioAdmin)