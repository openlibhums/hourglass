from django_components import component


@component.register("reference_list_item")
class ReferenceListItem(component.Component):

    template_name = "reference/list-item.html"
