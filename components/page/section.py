from django_components import component


@component.register("page_section")
class PageSection(component.Component):
    """
    Example usage:
    {% component_block "page_section" prose=False anchor="right" width="full" %}

    {% endcomponent_block %}
    """

    template_name = "page/section.html"

    def get_context_data(self, prose=True, anchor="left", width="part"):
        return {
            "prose": prose,
            "anchor": anchor,
            "width": width,
        }
