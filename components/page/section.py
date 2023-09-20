from django_components import component


@component.register("page_section")
class PageSection(component.Component):

    template_name = "page/section.html"

    def get_context_data(self, prose=True, anchor="left"):
        return {
            "prose": prose,
            "anchor": anchor,
        }
