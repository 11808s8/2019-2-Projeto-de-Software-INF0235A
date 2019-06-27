from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField

import json
from django.core.serializers.json import DjangoJSONEncoder


@register_snippet
class Category(models.Model):
    name = models.CharField(max_length=255)
    category_type = models.CharField(max_length=255)
    # slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('category_type'),
    ]


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class FormIndexPage(Page):
    template = "form/form_index_page.html"
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(self, request, *args, **kwargs)
        query_renda = list(Category.objects.all().filter(category_type="renda").values_list('name', 'category_type'))
        query_despesa = list(Category.objects.all().filter(category_type="despesa").values_list('name','category_type'))
        lista_renda = []
        lista_despesa = []
        # print(query_renda)
        # for linha in query_renda:
        #     lista_renda.append([linha[0],linha.category_type])
        # for linha in query_despesa:
        #     lista_despesa.append([linha.name, linha.category_type])
        lista_renda = json.dumps(query_renda, cls=DjangoJSONEncoder)
        lista_despesa = json.dumps(query_despesa, cls=DjangoJSONEncoder)
        # print(lista_renda)
        context["categories_renda"] = lista_renda
        context["categories_despesa"] = lista_despesa
        return context
    