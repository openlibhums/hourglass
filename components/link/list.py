from django_components import component


@component.register("link_list")
class LinkList(component.Component):

    template_name = "link/list.html"
