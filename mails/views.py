from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect
from .tasks import subscriber_added


class IndexView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "mails/index.html", {})

    def post(self, *args, **kwargs):
        email = self.request.POST.get("email")
        subscriber_added.delay(email)
        return HttpResponseRedirect(self.request.path_info)
