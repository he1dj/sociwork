from django.urls import path

from sociwork.users.views import user_detail_view, user_redirect_view, user_update_view

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("/(?P<pk>[0-9a-f-]+)/$", view=user_detail_view, name="detail"),
]
