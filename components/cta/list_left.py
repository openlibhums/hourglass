from django_components import component


@component.register("cta_list_left")
class CTAListLeft(component.Component):

    template_name = "cta/list_left.html"

    def get_context_data(self, *args, **kwargs):
        width = kwargs.pop('width', 'part')
        context = super().get_context_data(*args, **kwargs)
        context['width'] = width
        return context
