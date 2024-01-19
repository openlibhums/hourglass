from django_components import component


@component.register("staff")
class Staff(component.Component):

    template_name = "user/staff.html"

    def get_context_data(self, *args, **kwargs):
        request = kwargs.get('request', None)
        context = super().get_context_data(*args, **kwargs)
        if request:
            context['groups'] = request.press.staffgroup_set.all()
        return context
