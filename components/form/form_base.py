from django_components import component
from django.forms import widgets


class FormBase(component.Component):

    def get_context_data(self, *args, **kwargs):
        form = kwargs.pop('form', None)
        context = super().get_context_data(*args, **kwargs)

        if not form:
            return context

        for field_name, field in form.fields.items():
            if isinstance(field.widget, widgets.CheckboxInput):
                form.fields[field_name].widget.attrs['class'] = '''
                    border-white bg-white
                '''
            elif isinstance(field.widget, widgets.Select):
                form.fields[field_name].widget.attrs['class'] = '''
                    bg-transparent w-full border-white
                    max-lg:placeholder:text-md lg:placeholder:text-lg
                    max-lg:text-md lg:text-lg
                    focus:ring-transparent focus:border-orange
                    text-white cursor-white placeholder:text-white
                    border-t-0 border-r-0 border-b-1 border-l-0
                '''
            elif isinstance(field.widget, widgets.Textarea):
                form.fields[field_name].widget.attrs['class'] = '''
                    bg-transparent w-full border-white
                    max-lg:placeholder:text-md lg:placeholder:text-lg
                    max-lg:text-md lg:text-lg
                    focus:ring-transparent focus:border-orange
                    text-white cursor-white placeholder:text-white
                    border-1
                '''
            else:
                form.fields[field_name].widget.attrs['class'] = '''
                    bg-transparent w-full border-white
                    max-lg:placeholder:text-md lg:placeholder:text-lg
                    max-lg:text-md lg:text-lg
                    focus:ring-transparent focus:border-orange
                    text-white cursor-white placeholder:text-white
                    border-t-0 border-r-0 border-b-1 border-l-0
                '''

        context['form'] = form
        return context
