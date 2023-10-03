from django_components import component
from django.forms import widgets


@component.register("form_input")
class FormInput(component.Component):

    template_name = "form/input.html"

    def get_context_data(self, *args, **kwargs):
        input_type = kwargs.pop('type', None)
        input_name = kwargs.pop('name', None)
        input_value = kwargs.pop('value', None)
        context = super().get_context_data(*args, **kwargs)
        context['input_type'] = input_type
        context['input_name'] = input_name
        context['input_value'] = input_value
        return context
