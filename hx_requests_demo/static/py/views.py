from django.contrib.auth import get_user_model
from hx_requests.views import HtmxViewMixin

from hx_requests_demo.base_views import FilteredListView
from hx_requests_demo.filtersets import UserFilterset


class UserListView(HtmxViewMixin, FilteredListView):
    model = get_user_model()
    template_name = "user_list.html"
    filterset_class = UserFilterset
    paginate_by = 20
