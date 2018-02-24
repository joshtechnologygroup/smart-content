from django.urls import path

from apps.content import views

urlpatterns = [
    path('', views.content_discovery_view, name="content_discovery"),
    path('<int:content_id>/<str:action>/', views.content_action_view, name="content_action")
]
