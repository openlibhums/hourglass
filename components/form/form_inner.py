from django_components import component
from themes.hourglass.components.form import form_base


@component.register("form_inner")
class FormInner(form_base.FormBase):

    template_name = "form/form_inner.html"
