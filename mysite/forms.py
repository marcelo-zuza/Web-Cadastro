from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto


class ContatoForm(forms.Form):
    nome = forms.CharField(
        label='Nome',
        max_length=30,
        min_length=5,
    )

    email = forms.EmailField(
        label='Email',
        max_length=30,
        min_length=8
    )

    assunto = forms.CharField(
        label='Assunto',
        max_length=200,

    )

    # Nesse caso precisa usar o 'widget' para ampliar
    # A caixa de texto para caber o texto da mensagem
    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(),
        max_length=1000
    )

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='Email enviado pelo sistema Django',
            body=conteudo,
            from_email='contato@seudominio.com',
            to=['seuemail@servidor.com', 'outroemailsetiver@servidor.com'],
            headers={'Reply-To': email}

        )
        mail.send()

# se usa esse sufixo 'ModelForm' para se diferenciar de 'Form'
# Pois tem comportamentos diferentes
class ProdutoModelForm(forms.ModelForm):
    # Criaremos uma subclasse de metadados
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']
