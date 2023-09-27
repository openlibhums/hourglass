from django_components import component
import json


@component.register("glide")
class Glide(component.Component):

    template_name = "glide/glide.html"

    def get_context_data(self, glide_id, glide_type, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['glide_id'] = glide_id
        context['glide_type'] = glide_type
        if glide_type == 'quotes':
            options = {
                'rewind': False,
            }
        elif glide_type == 'gallery':
            options = {
                'rewind': False,
                'gap': 24,
                'startAt': 1,
                'focusAt': 'center',
                'perView': 3,
                'breakpoints': {
                    '1024': {'perView': 2},
                    '768': {'perView': 1},
                }
            }
        context['options'] = json.dumps(options)
        return context
