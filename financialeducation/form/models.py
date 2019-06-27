from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField


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
    