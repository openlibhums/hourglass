from django_components import component
from django.forms import widgets


class FormBase(component.Component):

    def get_context_data(self, *args, **kwargs):
        form = kwargs.pop('form', None)
        context = super().get_context_data(*args, **kwargs)

        if not form:
            return context

        for field_name, field in form.fields.items():
            tailwind = '''
                bg-transparent border-white w-full
                text-white cursor-white placeholder:text-white
                max-lg:placeholder:text-md lg:placeholder:text-lg
                max-lg:text-md lg:text-lg
                focus:ring-transparent focus:border-orange
            '''
            if isinstance(field.widget, widgets.Select):
                form.fields[field_name].widget.attrs['class'] = tailwind + '''
                    border-t-0 border-r-0 border-b-1 border-l-0
                '''
            elif isinstance(field.widget, widgets.Textarea):
                form.fields[field_name].widget.attrs['class'] = tailwind + '''
                    border-1
                '''
            else:
                form.fields[field_name].widget.attrs['class'] = tailwind + '''
                    border-t-0 border-r-0 border-b-1 border-l-0
                '''

        context['form'] = form
        return context
