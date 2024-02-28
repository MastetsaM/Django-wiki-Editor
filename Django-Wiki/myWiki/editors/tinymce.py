from django import forms
from wiki.editors.base import BaseEditor
from ckeditor.widgets import CKEditorWidget
from tinymce.widgets import AdminTinyMCE, TinyMCE


class MyTinyMCE(BaseEditor):
    editor_id = "tinymce"

    def get_admin_widget(self, revision=None):
        return AdminTinyMCE()

    def get_widget(self, revision=None):
        return TinyMCE()

