from django_components import component
from django.forms import widgets


@component.register("form_input")
class FormInput(component.Component):

    template_name = "form/input.html"

    def get_context_data(self, *args, **kwargs):
        input_id = kwargs.pop('id', '')
        input_type = kwargs.pop('type', 'text')
        input_name = kwargs.pop('name', '')
        input_value = kwargs.pop('value', '')
        aria_label = kwargs.pop('label', '')
        placeholder = kwargs.pop('placeholder', '')
        context = super().get_context_data(*args, **kwargs)
        context['input_id'] = input_id
        context['input_type'] = input_type
        context['input_name'] = input_name
        context['input_value'] = input_value
        context['aria_label'] = aria_label
        context['placeholder'] = placeholder
        return context
