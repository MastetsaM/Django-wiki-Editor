from myWiki import forms
from wiki.views import article

class Create(article.Create):
    form_class = forms.TinyMCE.MyCreateForm

class Edit(article.Edit):
    form_class = forms.TinyMCE.MyEditForm

class CreateRootView(article.CreateRootView):
    form_class = forms.TinyMCE.MyCreateRootForm
    