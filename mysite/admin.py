from django.contrib import admin
from .models import Produto

# Crie uma classe 'admin' correspondendo aos atributos criados em 'models'
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'imagem')

# Register your models here.
