from django_components import component
from django.forms import widgets


@component.register("form_field")
class FormField(component.Component):

    template_name = "form/field.html"

    def get_context_data(self, *args, **kwargs):
        field = kwargs.pop('field', None)
        if field:
            id_for_label = field.id_for_label
            label = field.label if not field.is_hidden else None
            errors = field.errors
            help_text = field.errors
            required = field.field.required
        else:
            id_for_label = kwargs.pop('id_for_label', None)
            label = kwargs.pop('label', None)
            errors = kwargs.pop('errors', None)
            help_text = kwargs.pop('help_text', None)
            required = kwargs.pop('required', None)
        context = super().get_context_data(*args, **kwargs)
        context['field'] = field
        context['id_for_label'] = id_for_label
        context['label'] = label
        context['errors'] = errors
        context['help_text'] = help_text
        context['required'] = required
        return context
