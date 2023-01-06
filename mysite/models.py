from django.db import models
# Módulo necessário para uso de imagens
from stdimage.models import StdImageField

#
from django.db.models import signals
from django.template.defaultfilters import slugify

# essa é uma classe abstrata feita para registro de informção em relação
# às modificações dos dados


class Base(models.Model):
    criado = models.DateField(
        'Data de criação',
        auto_now_add=True
    )

    modificado = models.DateField(
        'Data de Atualização',
        auto_now_add=True
    )

    # Essa é uma classe abstrata
    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField(
        'Nome do Produto',
        max_length=50,
        null=False,
        blank=False
    )

    preco = models.DecimalField(
        'Preço',
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,

    )

    estoque = models.IntegerField(
        'Estoque',
        default=0

    )

    # Assim se insere uma imagem
    imagem = StdImageField(
        'Imagem',
        upload_to='produtos',
        variations={'thumb': (124, 124)},

    )
    # 'slug' é uma ferramenta que faz com que a página seja criada com o nome do produto titulo
    slug = models.SlugField(
        'Slug',
        max_length=100,
        blank=True,
        editable=False

    )

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

# Esse comando faz com que antes de salvar o dado no seu banco de dados
# esse método será executado.
# Isso estanciará cada item com o nome adaptado para funcionar no sistema

signals.pre_save.connect(produto_pre_save, sender=Produto)
