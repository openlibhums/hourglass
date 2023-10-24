from django_components import component


@component.register("filterable_list")
class FilterableList(component.Component):

    template_name = "filterable/list.html"

    def get_context_data(self, list_id, value_names, *args, **kwargs):
        placeholder = kwargs.pop('placeholder', 'Filter')
        context = super().get_context_data(*args, **kwargs)
        context['list_id'] = list_id
        context['value_names'] = value_names
        context['placeholder'] = placeholder
        return context
