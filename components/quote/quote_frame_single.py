from django_components import component


@component.register("quote_frame_single")
class QuoteFrameSingle(component.Component):

    template_name = "quote/quote_frame_single.html"
