from django.forms import CharField
from django.utils.translation import gettext_lazy as _
from wiki import forms
from ckeditor.widgets import CKEditorWidget
from tinymce.widgets import TinyMCE

class CKEditor:
    class MyEditForm(forms.EditForm):
        content = CharField(
            label=_("Contents"),
            required=False,
            widget=CKEditorWidget(),
        )

    class MyCreateForm(forms.CreateForm):
        content = CharField(
            label=_("Contents"),
            required=False,
            widget=CKEditorWidget(),
        )

    class MyCreateRootForm(forms.CreateRootForm):
        content = CharField(
            label=_("Contents"),
            help_text=_(
                "<u>teste</u> This is just the initial contents of your article. After creating it, you can use more complex features like adding plugins, meta data, related articles etc..."
            ),
            required=False,
            widget=CKEditorWidget(),
        )

class TinyMCE:
    class MyEditForm(forms.EditForm):
        content = CharField(
            label=_("Contents"),
            required=False,
            widget=TinyMCE(),
        )

    class MyCreateForm(forms.CreateForm):
        content = CharField(
            label=_("Contents"),
            required=False,
            widget=TinyMCE(),
        )

    class MyCreateRootForm(forms.CreateRootForm):
        content = CharField(
            label=_("Contents"),
            help_text=_(
                "<u>teste</u> This is just the initial contents of your article. After creating it, you can use more complex features like adding plugins, meta data, related articles etc..."
            ),
            required=False,
            widget=TinyMCE(),
        )



