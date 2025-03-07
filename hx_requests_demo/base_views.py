from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from hx_requests.views import HtmxViewMixin

from hx_requests_demo.filtersets import UserFilterset


# Create your views here.
class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(
            queryset=queryset, **self.get_filterset_kwargs()
        )
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context["filterset"] = self.filterset
        return context

    def get_filterset_kwargs(self):
        return {
            "data": self.request.GET or {},
            "request": self.request,
        }
