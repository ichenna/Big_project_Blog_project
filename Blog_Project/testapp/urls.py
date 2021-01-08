from . import views
from django.urls import path


urlpatterns = [
    path("", views.post_list_view),
    path('tag/(?P<tag_slug>[-\w]+)/', views.post_list_view, name='post_list_by_tag_name'),
    path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/', views.post_detail_view, name='post_detail'),
    path("<int:id>/share/", views.mail_send_view, name="share")

]



