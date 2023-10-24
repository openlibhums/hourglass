from django_components import component


@component.register("cta_list_item_left")
class CTAListItemLeft(component.Component):

    template_name = "cta/list_item_left.html"
