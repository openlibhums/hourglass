from django_components import component


@component.register("staff_page")
class StaffPage(component.Component):

    template_name = "staff/page.html"

    def get_context_data(self, *args, **kwargs):
        request = kwargs.get('request', None)
        context = super().get_context_data(*args, **kwargs)
        if request:
            context['staff_groups'] = request.press.staffgroup_set.all()
        return context
