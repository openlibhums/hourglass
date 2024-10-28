from django_components import component


@component.register("button_group")
class ButtonGroup(component.Component):

    template_name = "form/button-group.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
