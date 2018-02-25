from django.urls import path

from apps.contract import views

urlpatterns = [
		path("<int:contract>/content/<int:content>/<str:action>/", views.associate_action_with_contract_view),
		path("execute/", views.execute_contract)
]
