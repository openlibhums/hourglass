from django_components import component


@component.register("cta_list_item")
class CTAListItem(component.Component):

    template_name = "cta/list_item.html"
