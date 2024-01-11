from django_components import component


@component.register("staff_group")
class StaffGroup(component.Component):

    template_name = "staff/group.html"

    def get_context_data(self, *args, **kwargs):
        group = kwargs['group']
        context = super().get_context_data(*args, **kwargs)
        context['group'] = group
        return context
