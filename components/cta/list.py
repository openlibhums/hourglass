from django_components import component


@component.register("cta_list")
class CTAList(component.Component):

    template_name = "cta/list.html"
