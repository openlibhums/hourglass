from django_components import component
from themes.hourglass.components.form import form_base


@component.register("form")
class Form(form_base.FormBase):

    template_name = "form/form.html"

    def get_context_data(self, *args, **kwargs):
        form_action = kwargs.pop('form_action', '')
        form_method = kwargs.pop('form_method', '')
        notify_required = kwargs.pop('notify_required', True)
        default_button = kwargs.pop('default_button', True)
        enctype = kwargs.pop('enctype', '')
        context = super().get_context_data(*args, **kwargs)

        context['form_method'] = form_method
        context['form_action'] = form_action
        context['notify_required'] = notify_required
        context['default_button'] = default_button
        context['enctype'] = enctype

        return context
