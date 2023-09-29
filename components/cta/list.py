from django_components import component


@component.register("cta_list")
class CTAList(component.Component):

    template_name = "cta/list.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)
