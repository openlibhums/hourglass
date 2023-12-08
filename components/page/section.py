from django_components import component


@component.register("page_section")
class PageSection(component.Component):
    """
    Example usage:
    {% component_block "page_section" prose=False anchor="right" width="full" %}
      ...
    {% endcomponent_block %}
    """

    template_name = "page/section.html"

    def get_context_data(self, *args, **kwargs):
        return {
            "prose": kwargs.pop("prose", True),
            "anchor": kwargs.pop("anchor", "left"),
            "width": kwargs.pop("width", "part"),
            "colors": kwargs.pop("colors", "light"),
            "labelledby": kwargs.pop("labelledby", ""),
            "label": kwargs.pop("label", ""),
            "element": kwargs.pop("element", "section"),
        }
