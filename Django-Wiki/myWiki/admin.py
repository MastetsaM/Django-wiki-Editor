from django.contrib import admin
from myWiki import models
import wiki.admin as wikiAdmin
from ckeditor.widgets import CKEditorWidget
# Register your models here.
    

class ArticleRevisionForm(wikiAdmin.ArticleRevisionForm):
    class Meta:
        model = models.MyArticleRevision
        exclude = ()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget = CKEditorWidget()
        self.fields["content2"].widget = CKEditorWidget()



class MyArticleRevisionAdmin(wikiAdmin.ArticleRevisionAdmin):
    list_display = ("title", "created", "modified", "user", "ip_address")
    form = ArticleRevisionForm


admin.site.register(models.MyArticleRevision, MyArticleRevisionAdmin)
