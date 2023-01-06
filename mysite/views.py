from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages
from .forms import ProdutoModelForm
from .models import Produto


def index(request):
    context = {
        'produto': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'Mensagem enviado com SUCESSO')
            form = ContatoForm()

        else:
            messages.error(request, 'Envio de mensagem FALHOU')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com SUCESSO')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'ERRO ao cadastrar o produto')
    else:
        form = ProdutoModelForm()
    context = {
        'form': form
    }

    return render(request, 'produto.html', context)
