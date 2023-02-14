from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['titulo_post', 'excerto_post', 'conteudo_post', 'autor_post', 'categoria_post', 'imagem_post', 'publicado_post']

        widgets = {
            
            'titulo_post': forms.TextInput(attrs={'placeholder':'Titulo', 'class': 'form-control form-control-lg'}),
            'excerto_post': forms.TextInput(attrs={'placeholder':'Súmario', 'class': 'form-control form-control-lg'}),
            'conteudo_post':SummernoteWidget(),
            'autor_post': forms.Select(attrs={'placeholder':'Post', 'class': 'form-control form-control-lg'}),
            'categoria_post': forms.Select(attrs={'placeholder':'Post', 'class': 'form-control form-control-lg'}),
            'imagem_post': forms.FileInput(attrs={'id':'validatedCustomFile'}),
            '': forms.CheckboxInput(attrs={'class': 'required checkbox form-control'}),
            
        }
