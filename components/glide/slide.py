from django_components import component


@component.register("glide_slide")
class GlideSlide(component.Component):

    template_name = "glide/slide.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)
