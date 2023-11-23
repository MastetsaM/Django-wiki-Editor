from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _

from wiki.models import article

# Create your models here.

class MyArticleRevision(article.ArticleRevision):
    content2 = models.TextField(blank=True, verbose_name=_("article contents"), null=True)

