from django_components import component


@component.register("reference_list")
class ReferenceList(component.Component):

    template_name = "reference/list.html"
