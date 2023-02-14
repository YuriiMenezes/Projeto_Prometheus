from django.forms import ModelForm
from .models import Comentario
import requests



class FormComentario(ModelForm):
    def clean(self):

        #declaarando as variaveis para autenticação do Recapcha
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')
        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LdmuVgdAAAAAJ9oVtnNSmYLwwSRjQhWSA2KUOP2', # secret key do google recapcha
                'response': recaptcha_response                        # variavel que recebe a requisicao do fronte 
            }
        )

        recaptcha_result = recaptcha_request.json()

        print(recaptcha_result)
        
        print(recaptcha_result.get('success'))


        

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais que 5 caracteres.'
            )

        #Mensagem de erro caso o recapcha não for correspondente
        if not recaptcha_result.get('success'):
            self.add_error(
                'comentario',
                'Desculpe, o reCAPCHA não correnponde.'
            )    

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')
