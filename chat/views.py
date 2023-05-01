from django.views.generic import TemplateView
from django.utils.safestring import mark_safe
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Calls
import json


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["chats"] = self.request.user.answered_calls.all() if self.request.user.is_staff else self.request.user.calls.all()
        return context


class SalaView(LoginRequiredMixin, TemplateView):
    template_name = 'sala.html'

    def get_context_data(self, **kwargs):
        context = super(SalaView, self).get_context_data(**kwargs)
        context['room_name'] = mark_safe(
            json.dumps(self.kwargs['room_name'])
        )
        return context