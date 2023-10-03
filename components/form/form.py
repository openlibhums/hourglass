from django_components import component
from themes.hourglass.components.form import form_base


@component.register("form")
class Form(form_base.FormBase):

    template_name = "form/form.html"

    def get_context_data(self, *args, **kwargs):
        form_action = kwargs.pop('form_action', '')
        form_method = kwargs.pop('form_method', '')
        enctype = kwargs.pop('enctype', '')
        context = super().get_context_data(*args, **kwargs)

        context['form_method'] = form_method
        context['form_action'] = form_action
        context['enctype'] = enctype
        return context
