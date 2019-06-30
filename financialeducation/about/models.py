from django.db import models

from wagtail.core.models import Page

class About(Page):
    template = "about/sobre.html"