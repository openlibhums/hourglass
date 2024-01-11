from django_components import component


@component.register("page_intro")
class PageIntro(component.Component):

    template_name = "page/intro.html"

    def get_context_data(self, *args, **kwargs):
        color = kwargs.pop('color', 'blue')
        label = kwargs.pop('label', 'About')
        context = super().get_context_data(*args, **kwargs)
        context['color'] = color
        context['label'] = label
        return context
