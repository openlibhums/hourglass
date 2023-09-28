from django_components import component


@component.register("cta_list_three")
class CTAListThree(component.Component):

    template_name = "cta/list_three.html"

    def get_context_data(self):
        return {}
