from django.db import models

# Create your models here.

from blog_posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

class Comentario(models.Model):

    nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
    email_comentario = models.EmailField(verbose_name='E-mail')
    comentario = models.TextField(verbose_name='Comentário')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_comentario = models.DateTimeField(default=timezone.now)
    publicad_comentario = models.BooleanField(default=False) # lembrar na hora de refatorar de colocar o nome Publicado_comentario

    def __str__(self):
        return self.nome_comentario    