from django_components import component


@component.register("infographic_grid")
class InfographicGrid(component.Component):

    template_name = "infographic/grid.html"

    def get_context_data(self, *args, **kwargs):
        return {
            'ordered': kwargs.get('ordered', True)
        }
