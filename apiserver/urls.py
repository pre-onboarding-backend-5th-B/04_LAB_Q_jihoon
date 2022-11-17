from django.urls import path
from apiserver import views
urlpatterns = [
    path("seoul/", views.GuInfoApiView.as_view(), name="gu_info"),
    path("seoul/<int:gu_id>/", views.GuInfoDetailApiView.as_view(), name="gu_data")
]
