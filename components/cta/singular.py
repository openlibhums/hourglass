from django_components import component


@component.register("cta_singular")
class CTASingular(component.Component):

    template_name = "cta/singular.html"

    def get_context_data(self):
        return {}
