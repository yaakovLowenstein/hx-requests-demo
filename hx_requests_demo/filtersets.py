import django_filters
from django.contrib.auth import get_user_model


class UserFilterset(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr="icontains", label="Username")
    email = django_filters.CharFilter(lookup_expr="icontains", label="Email")
    first_name = django_filters.CharFilter(lookup_expr="icontains", label="First Name")
    last_name = django_filters.CharFilter(lookup_expr="icontains", label="Last Name")

    @property
    def qs(self):
        return super().qs.order_by("username")

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name"]
