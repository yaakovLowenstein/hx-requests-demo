from hx_requests.hx_requests import BaseHxRequest, DeleteHxRequest, FormModalHxRequest

from hx_requests_demo.forms import UserForm


class InfiniteScroll(BaseHxRequest):
    name = "infinite_scroll"
    GET_template = "user_list.html"
    GET_block = "items"


class Filter(BaseHxRequest):
    name = "filter"
    GET_template = "user_list.html"
    GET_block = ["table", "total"]


class UpdateUser(FormModalHxRequest):
    name = "update_user"
    form_class = UserForm
    title = "User Form"
    hx_object_name = "object"
    GET_template = "update_form.html"
    POST_template = "user_list.html"
    POST_block = "row"

    # This is how I would do it if the object list had other
    # attributes appened to each item I.e. prefetches that
    # use the to_attr argument

    # def get_context_on_POST(self, **kwargs):
    #     context= super().get_context_on_POST(**kwargs)
    #     context['object'] = self.view.filterset.qs.get(pk=self.hx_object.pk)
    #     return


class CreateUser(FormModalHxRequest):
    name = "create_user"
    form_class = UserForm
    title = "User Form"
    GET_template = "create_form.html"
    POST_template = "user_list.html"
    POST_block = ["table", "total"]
    refresh_views_context_on_POST = True


class DeleteUser(DeleteHxRequest):
    name = "delete_user"
    POST_template = "user_list.html"
    POST_block = ["total"]
    refresh_views_context_on_POST = True
