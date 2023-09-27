from django_components import component


@component.register("glide")
class Glide(component.Component):

    template_name = "glide/glide.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)
