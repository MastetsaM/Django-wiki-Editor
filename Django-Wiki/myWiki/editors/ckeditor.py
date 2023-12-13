from django import forms
from wiki.editors.base import BaseEditor
from ckeditor.widgets import CKEditorWidget


class MyCkeditor(BaseEditor):
    editor_id = "ckeditor"

    def get_admin_widget(self, revision=None):
        return CKEditorWidget()

    def get_widget(self, revision=None):
        return CKEditorWidget()

    class AdminMedia:
        CKEditorMedia = CKEditorWidget().media
        css = CKEditorMedia._css
        js = CKEditorMedia._js

    class Media:
        CKEditorMedia = CKEditorWidget().media
        css = CKEditorMedia._css
        js = CKEditorMedia._js
