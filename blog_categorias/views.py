
from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from blog_posts.models import Post
from blog_posts.forms import PostForm

from django.db.models import Q, Count, Case, When
from blog_comentarios.forms import FormComentario
from blog_comentarios.models import Comentario
from django.contrib import messages




class CategoriasIndex(ListView):
    
   model = Post #model usado para preencher 
   template_name = 'blog_categorias/categoria_index.html'#direcionando para o template
   paginate_by = 6 # quantos posts vao ficar na pagina
   context_object_name = 'posts'#objeto de busca

   #funcao para colocar os posts em ordem do ultimo adicionado(mais recente)
   def get_queryset(self):
       qs = super().get_queryset()# refazendo o query set com a variavel qs
       qs = qs.order_by('-id').filter(publicado_post=True)#ordenando os posts na variavel qs e faz a busca apenas nos postes publicados

       qs = qs.annotate(# parte da funçao que separa os comentarios publicados

           numero_comentarios=Count( #Count = contar
               Case( #Case = caso
                   When(comentario__publicad_comentario=True, then=1) #when = quando obs : lembrar na hora de refatorar de colocar o nome Publicado_comentario

               )
           )

       )

       return qs

class windows(ListView):
    
   model = Post #model usado para preencher 
   template_name = 'blog_categorias/windows.html'#direcionando para o template
   paginate_by = 6 # quantos posts vao ficar na pagina
   context_object_name = 'posts'#objeto de busca

   #funcao para colocar os posts em ordem do ultimo adicionado(mais recente)
   def get_queryset(self):
       qs = super().get_queryset().filter(categoria_post=1)# 1 tecnologia refazendo o query set com a variavel qs
       qs = qs.order_by('-id').filter(publicado_post=True)#ordenando os posts na variavel qs e faz a busca apenas nos postes publicados

       qs = qs.annotate(# parte da funçao que separa os comentarios publicados

           numero_comentarios=Count( #Count = contar
               Case( #Case = caso
                   When(comentario__publicad_comentario=True, then=1) #when = quando obs : lembrar na hora de refatorar de colocar o nome Publicado_comentario

               )
           )

       )

       return qs


class novidades(ListView):

   model = Post #model usado para preencher 
   template_name = 'blog_categorias/novidades.html'#direcionando para o template
   paginate_by = 6 # quantos posts vao ficar na pagina
   context_object_name = 'posts'#objeto de busca

   #funcao para colocar os posts em ordem do ultimo adicionado(mais recente)
   def get_queryset(self):
       qs = super().get_queryset().filter(categoria_post=2)# 2 animes refazendo o query set com a variavel qs
       qs = qs.order_by('-id').filter(publicado_post=True)#ordenando os posts na variavel qs e faz a busca apenas nos postes publicados

       qs = qs.annotate(# parte da funçao que separa os comentarios publicados

           numero_comentarios=Count( #Count = contar
               Case( #Case = caso
                   When(comentario__publicad_comentario=True, then=1) #when = quando obs : lembrar na hora de refatorar de colocar o nome Publicado_comentario

               )
           )

       )

       return qs

   
class linux(ListView):

   model = Post #model usado para preencher 
   template_name = 'blog_categorias/linux.html'#direcionando para o template
   paginate_by = 6 # quantos posts vao ficar na pagina
   context_object_name = 'posts'#objeto de busca

   #funcao para colocar os posts em ordem do ultimo adicionado(mais recente)
   def get_queryset(self):
       qs = super().get_queryset().filter(categoria_post=3)# 3 tutoriais refazendo o query set com a variavel qs
       qs = qs.order_by('-id').filter(publicado_post=True)#ordenando os posts na variavel qs e faz a busca apenas nos postes publicados

       qs = qs.annotate(# parte da funçao que separa os comentarios publicados

           numero_comentarios=Count( #Count = contar
               Case( #Case = caso
                   When(comentario__publicad_comentario=True, then=1) #when = quando obs : lembrar na hora de refatorar de colocar o nome Publicado_comentario

               )
           )

       )

       return qs

class desenvolvimento(ListView): 

   model = Post #model usado para preencher 
   template_name = 'blog_categorias/desenvolvimento.html'#direcionando para o template
   paginate_by = 6 # quantos posts vao ficar na pagina
   context_object_name = 'posts'#objeto de busca

   #funcao para colocar os posts em ordem do ultimo adicionado(mais recente)
   def get_queryset(self):
       qs = super().get_queryset().filter(categoria_post=6)# 4 games refazendo o query set com a variavel qs
       qs = qs.order_by('-id').filter(publicado_post=True)#ordenando os posts na variavel qs e faz a busca apenas nos postes publicados

       qs = qs.annotate(# parte da funçao que separa os comentarios publicados

           numero_comentarios=Count( #Count = contar
               Case( #Case = caso
                   When(comentario__publicad_comentario=True, then=1) #when = quando obs : lembrar na hora de refatorar de colocar o nome Publicado_comentario

               )
           )

       )

       return qs


class tutoriais(ListView): 

   model = Post #model usado para preencher 
   template_name = 'blog_categorias/tutoriais.html'#direcionando para o template
   paginate_by = 6 # quantos posts vao ficar na pagina
   context_object_name = 'posts'#objeto de busca

   #funcao para colocar os posts em ordem do ultimo adicionado(mais recente)
   def get_queryset(self):
       qs = super().get_queryset().filter(categoria_post=5)# 4 filmes e series refazendo o query set com a variavel qs
       qs = qs.order_by('-id').filter(publicado_post=True)#ordenando os posts na variavel qs e faz a busca apenas nos postes publicados

       qs = qs.annotate(# parte da funçao que separa os comentarios publicados

           numero_comentarios=Count( #Count = contar
               Case( #Case = caso
                   When(comentario__publicad_comentario=True, then=1) #when = quando obs : lembrar na hora de refatorar de colocar o nome Publicado_comentario

               )
           )

       )

       return qs       
