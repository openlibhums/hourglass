from django_components import component


@component.register("page_intro")
class PageIntro(component.Component):

    template_name = "page/intro.html"

    def get_context_data(self):
        return {}
