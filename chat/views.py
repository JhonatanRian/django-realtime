from django.views.generic import TemplateView
from django.utils.safestring import mark_safe
import json

class IndexView(TemplateView):
    template_name = 'index.html'


class SalaView(TemplateView):
    template_name = 'sala.html'

    def get_context_data(self, **kwargs):
        context = super(SalaView, self).get_context_data(**kwargs)
        context['room_name'] = mark_safe(
            json.dumps(self.kwargs['room_name'])
        )
        return context