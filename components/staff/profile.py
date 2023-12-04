from django_components import component


@component.register("staff_profile")
class StaffProfile(component.Component):

    template_name = "staff/profile.html"

    def get_context_data(self, *args, **kwargs):
        user = kwargs.pop('user', '')
        context = super().get_context_data(*args, **kwargs)
        context['user'] = user
        return context
