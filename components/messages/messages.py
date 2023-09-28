from django_components import component
from django.contrib import messages


@component.register("messages")
class Messages(component.Component):

    template_name = "messages/messages.html"

    def get_context_data(self, messages, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['messages'] = messages
        return context
