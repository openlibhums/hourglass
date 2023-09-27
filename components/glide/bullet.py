from django_components import component


@component.register("glide_bullet")
class GlideBullet(component.Component):

    template_name = "glide/bullet.html"

    def get_context_data(self, slide_index, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['slide_index'] = slide_index
        return context
