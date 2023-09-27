from django_components import component


@component.register("quote")
class Quote(component.Component):

    template_name = "quote/quote.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)
